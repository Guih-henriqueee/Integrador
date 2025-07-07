import time
from Services.UpdateOrdersPending import atualizar_pedidos_com_status_pendente 

def ReconsultarPedidosPendentes():
    tempo = 30
    intervalo_reconsulta = tempo * 60 
    while True:
        try:
            atualizar_pedidos_com_status_pendente() 
        except Exception as e:
            print(f"❌ Erro na rotina de reconsulta: {e}")
        
        time.sleep(intervalo_reconsulta)
