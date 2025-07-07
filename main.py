from concurrent.futures import ThreadPoolExecutor
from Services.Integrador import ProcessPainels
from Services.UpdateRoutine import atualizar_pedidos_com_status_pendente
from Utils.LoginService import validar_todas_tabelas  
from Helper.Settings import *

if __name__ == "__main__":
    print("🔄 [POSTGRES] - Iniciando teste de conexão com banco de dados...")

    try:
        with test_get_conn() as conn:  
            print("✅ [POSTGRES] - Conexão bem-sucedida!")

            print("🔄 [POSTGRES] - Validando estrutura das tabelas no banco...")
            resultados = validar_todas_tabelas(conn)

            if not resultados:
                print("❌ [POSTGRES] - Estrutura de tabelas não validada. Verifique o schema.")
                exit(1)

    except Exception as e:
        print(f"❌ [SERVICE] - Falha ao validar estrutura ou conectar: {e}")
        exit(1)

    print("🔄 [SERVICE] - Iniciando integração e atualização de pedidos...")

    with ThreadPoolExecutor(max_workers=3) as executor:
     
        for config in API_CONFIGS:
            executor.submit(ProcessPainels, config)
        
 
        executor.submit(atualizar_pedidos_com_status_pendente)


    print("✅ [SERVICE] - Rotinas iniciadas: integração e atualização.")
