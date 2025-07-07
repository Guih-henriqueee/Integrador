from enum import Enum

class LogMessage(Enum):
    INICIO_RECONSULTA = "Iniciando reconsulta do pedido {pedido_id}"
    FIM_RECONSULTA = "Reconsulta concluída para pedido {pedido_id}"
    ERRO_RECONSULTA = "Erro ao reconsultar pedido {pedido_id}: {erro}"

    ENVIO_PEDIDO = "Enviando pedido {pedido_id} ao painel {painel}"
    SUCESSO_ENVIO = "Pedido {pedido_id} integrado com sucesso no painel {painel}"
    FALHA_ENVIO = "Falha ao integrar pedido {pedido_id} no painel {painel}: {erro}"

    CONEXAO_DB = "Conexão com banco estabelecida"
    FALHA_CONEXAO_DB = "Erro ao conectar ao banco: {erro}"

    INICIO_PROCESSO = "🔄 Início do processo para painel {painel}"
    FIM_PROCESSO = "✅ Fim do processo para painel {painel}"
