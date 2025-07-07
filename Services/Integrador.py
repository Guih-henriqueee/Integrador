import requests
import psycopg2
import json
import time
from Services.SignUpLog import registrar_log
from Services.InsertOrder import inserir_pedido, inserir_itens
from Services.OrderStarter import verifica_pedido, buscar_ultimo_id_por_painel
from Helper.ConnectionDB import  get_conn
from Helper.Settings import *
from Utils.Builders import Builder_Shopee, Builder_MercadoLivre, Builder_Base, Builder_Items

BUILDERS = {
    "Shopee": Builder_Shopee,
    "Mercado Livre": Builder_MercadoLivre,
 }




def ProcessPainels(Settings):
        painel = Settings.get("painel")
        start_order = Settings.get("start_order")
        
        print(f"🔄 [POSTGRES] - Localizando último pedido integrado para painel {painel}...")
        with get_conn() as conn:
            
            try:
                ultimo_id = buscar_ultimo_id_por_painel(conn, painel)
                
                ultimo_id = ultimo_id["id"] if ultimo_id else 0
            except Exception as e:
                print(f"❌ Erro ao buscar último ID do painel {painel}: {e}")
                ultimo_id = 0
        print(f"🔎 [POSTGRES] - Último pedido integrado: {ultimo_id}")

        if start_order is not None:
            try:
                inicio_consumo = max(start_order, ultimo_id + 1)
                print(f"🔄 [PRECODE {painel}] - Integrando pedidos do painel {painel} a partir do pedido {inicio_consumo}")
                
                try:
                    consumir_pedidos_por_id_com_Settings(Settings, inicio_consumo)  
                except Exception as e:
                    print(conn, None, "erro", f"❌ [PRECODE] Erro na integração do painel {painel}: {e}")    
            except Exception as e:
                with get_conn() as conn:
                    registrar_log(conn, None, "erro", f"❌ [PRECODE] Erro na integração do painel {painel}: {e}")
                print(f"❌ [PRECODE {painel}] - Erro durante a integração: {e}")
        else:
            intervalo_pausa = 60 / Settings["limite_por_minuto"]
            with get_conn() as conn:
                registrar_log(conn, None, "erro", f"❌ [PRECODE] Intervalo de pedidos não definido para painel {painel}")
            print(f"⚠️ [PRECODE {painel}] - Painel ignorado por falta de start_order.")
            time.sleep(intervalo_pausa)
            
        
def consumir_pedidos_por_id_com_Settings(Settings, inicio_id: int):
    intervalo_pausa = 60 / Settings["limite_por_minuto"]
    base_url = Settings["base_url"]
    token = Settings["token"]
    painel = Settings["painel"]
    codigoPedido = inicio_id
    standby_time = 30 * 60  

    while True:
        url = f"{base_url}/{codigoPedido}"
        try:
            response = requests.get(url, headers={"Authorization": f"Basic {token}"})
        except requests.RequestException as e:
            print(f"[PRECODE {painel}] - Erro de requisição no pedido {codigoPedido}: {e}")
            with get_conn() as conn:
                registrar_log(conn, codigoPedido, "erro", f"Erro de requisição: {e}")
            time.sleep(intervalo_pausa)
            continue

        if response.status_code == 404:
            print(f"[PRECODE {painel}] - Pedido {codigoPedido} não encontrado (404). Ignorando.")
            with get_conn() as conn:
                registrar_log(conn, codigoPedido, "erro", "Pedido não encontrado (404)")
            time.sleep(intervalo_pausa)
            codigoPedido += 1
            continue

        if response.status_code != 200:
            print(f"[PRECODE {painel}] - Erro HTTP {response.status_code} no pedido {codigoPedido}: {response.text}")
            with get_conn() as conn:
                registrar_log(conn, codigoPedido, "erro", f"HTTP {response.status_code}: {response.text}")
            time.sleep(intervalo_pausa)
            continue

        pedido_raw = response.json()
        lista_pedidos = pedido_raw.get("pedido", [])

        if not lista_pedidos:
            print(f"⏳ [PRECODE {painel}] - Pedido {codigoPedido} retornou payload vazio. Entrando em standby por 30 minutos.")
            with get_conn() as conn:
                registrar_log(conn, codigoPedido, "info", "Payload vazio - standby por 30 minutos")
            time.sleep(standby_time)
            continue

        pedido = lista_pedidos[0]
        canal = pedido.get("nomeAfiliado")
        builder_func = BUILDERS.get(canal, Builder_Base)

        if canal not in BUILDERS:
            with get_conn() as conn:
                registrar_log(conn, codigoPedido, "aviso", f"Canal '{canal}' não parametrizado. Usando builder base.")
            print(f"⚠️  [PRECODE {painel}] - Canal '{canal}' não parametrizado. Usando builder base para pedido {codigoPedido}.")

        registro = builder_func(pedido, codigoPedido, painel)
        
        with get_conn() as conn:
            pedido_exist = verifica_pedido(conn, painel, codigoPedido)
            pedido_exist = pedido_exist["id"] if pedido_exist else 0

            if codigoPedido != pedido_exist:
                try:
                    inserir_pedido(conn, registro)
                    itens_formatados = Builder_Items(pedido, codigoPedido, painel)
                    inserir_itens(conn, codigoPedido, itens_formatados)
                    registrar_log(conn, codigoPedido, "sucesso", f"Pedido integrado com sucesso", painel)
                    print(f"✅ [PRECODE {painel}] - Pedido {codigoPedido} integrado com sucesso")
                except psycopg2.errors.UniqueViolation:
                    conn.rollback()
                    registrar_log(conn, codigoPedido, "duplicado", f"Pedido já existente")
                    print(f"⚠️ [PRECODE {painel}] - Pedido {codigoPedido} já existe (duplicado)")
                except Exception as e:
                    conn.rollback()
                    registrar_log(conn, codigoPedido, "erro", f"Erro ao inserir pedido: {str(e)}")
                    print(f"❌ [PRECODE {painel}] - Erro ao inserir pedido {codigoPedido}: {e}")
            else:
                print(f"[PRECODE {painel}] - Pedido {codigoPedido} já incluído anteriormente.")

        codigoPedido += 1
        time.sleep(intervalo_pausa)
