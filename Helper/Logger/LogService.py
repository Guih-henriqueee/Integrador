from Helper.Logger.Enum.LogMessages import LogMessage
from Helper.Logger.LoggerFactory import get_logger

def log_info(servico: str, mensagem: str):
    logger = get_logger(servico)
    logger.info(mensagem)

def log_warning(servico: str, mensagem: str):
    logger = get_logger(servico)
    logger.warning(mensagem)

def log_error(servico: str, mensagem: str):
    logger = get_logger(servico)
    logger.error(mensagem)

def log_debug(servico: str, msg_enum: LogMessage, **kwargs):
    logger = get_logger(servico)
    message = msg_enum.value.format(**kwargs)
    logger.debug(message)
