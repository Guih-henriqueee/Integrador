import time
from Services.UpdateOrdersPending import atualizar_pedidos_com_status_pendente 

def ReconsultarPedidosPendentes():
    intervalo_reconsulta = 30 * 60 

    while True:
        print("🔁 Iniciando rotina de reconsulta de pedidos pendentes...")
        try:
            atualizar_pedidos_com_status_pendente()
            print("✅ Reconsulta concluída com sucesso.")
        except Exception as e:
            print(f"❌ Erro na rotina de reconsulta: {e}")

        time.sleep(intervalo_reconsulta)
