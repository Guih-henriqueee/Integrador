import requests
import time
import psycopg2
from datetime import datetime
from Helper.ConnectionDB import get_conn, get_db_schema_info
from Helper.Settings import API_CONFIGS
from Services.SignUpLog import registrar_log
from Services.InsertOrder import atualizar_pedido, atualizar_itens
from Utils.Builders import Builder_Base, Builder_Shopee, Builder_MercadoLivre, Builder_Items
from Repository.Queryes.QueryCheckOrdersNew import ORDERS_NEW  
from Utils.QuoteSchema import quoted
tempo = 30
intervalo_reconsulta = tempo * 60 

BUILDERS = {
    "Shopee": Builder_Shopee,
    "Mercado Livre": Builder_MercadoLivre,
}

schema_config, table_orders, *_ = get_db_schema_info()
schema_config = quoted(schema_config)

def atualizar_pedidos_com_status_pendente():
    while True:    
        print("🔁 [RECONSULTA] - Iniciando rotina de reconsulta de pedidos pendentes...")
        with get_conn() as conn:
            cur = conn.cursor()
            try:
                query = ORDERS_NEW.format(SCHEMA=schema_config, TABLE=table_orders)
                cur.execute(query)
                pedidos_pendentes = cur.fetchall()
            except Exception as e:
                print(f"❌ [RECONSULTA] - Erro ao consultar pedidos pendentes: {e}")

        print(f"🔍 [RECONSULTA] - Encontrados {len(pedidos_pendentes)} pedidos pendentes para reconsulta.")
        atualizados = 0
        for pedido_id, painel in pedidos_pendentes:
            settings = next((s for s in API_CONFIGS if s["painel"] == painel), None)
            if not settings:
                print(f"⚠️ [PRECODE {painel}] - Configuração não encontrada. Ignorando pedido {pedido_id}.")
                continue

            intervalo_pausa = 60 / settings.get("limite_por_minuto", 30)

            try:
                url = f"{settings['base_url']}/{pedido_id}"
                response = requests.get(url, headers={"Authorization": f"Basic {settings['token']}"})

                if response.status_code != 200:
                    print(f"⚠️ [PRECODE {painel}] - Requisição falhou para pedido {pedido_id}: {response.status_code}")
                    time.sleep(intervalo_pausa)
                    continue

                pedido_raw = response.json()
                lista_pedidos = pedido_raw.get("pedido", [])

                if not lista_pedidos:
                    print(f"⚠️ [PRECODE {painel}] - Pedido {pedido_id} retornou payload vazio. Ignorado.")
                    time.sleep(intervalo_pausa)
                    continue

                pedido = lista_pedidos[0]
                status = int(pedido.get("codigoStatusAtual"))

                if status not in [1]:  # Reavalie essa regra conforme necessário
                    canal = pedido.get("nomeAfiliado")
                    builder_func = BUILDERS.get(canal, Builder_Base)
                    registro_atualizado = builder_func(pedido, pedido_id, painel)
                    update_date = datetime.now()
                    registro_atualizado["atualizado_em"] = update_date
                   

                    with get_conn() as conn_update:
                        try:
                            atualizar_pedido(conn_update, registro_atualizado)
                            itens_formatados = Builder_Items(pedido, pedido_id, painel)
                            for item in itens_formatados:
                                item["atualizado_em"] = update_date
                            atualizar_itens(conn_update, pedido_id, itens_formatados)

                            registrar_log(conn_update, pedido_id, "atualizacao", "Pedido atualizado via reconsulta", painel)
                            print(f"🔄 [PRECODE {painel}] - Pedido {pedido_id} atualizado com sucesso.")
                            atualizados += 1
                        except Exception as e:
                            conn_update.rollback()
                            registrar_log(conn_update, pedido_id, "erro", f"Erro na atualização: {e}")
                            print(f"❌ [PRECODE {painel}] - Erro ao atualizar pedido {pedido_id}: {e}")

                time.sleep(intervalo_pausa)

            except Exception as e:
                print(f"❌ [PRECODE {painel}] - Erro na reconsulta do pedido {pedido_id}: {e}")
                time.sleep(intervalo_pausa)
        print(f"⏳ [RECONSULTA] - Resultado da Atualização {atualizados}/{len(pedidos_pendentes)} ...")    
        
        print(f"⏳ [RECONSULTA] - Aguardando {tempo} minutos para próxima reconsulta...")   
        print("✅ [RECONSULTA] - Reconsulta concluída com sucesso.")
        time.sleep(intervalo_reconsulta)
        