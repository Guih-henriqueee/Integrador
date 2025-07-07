import logging
from logging.handlers import TimedRotatingFileHandler
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

def get_logger(servico_nome: str) -> logging.Logger:
    logger = logging.getLogger(servico_nome)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = TimedRotatingFileHandler(
            filename=os.path.join(log_dir, f"{servico_nome}.log"),
            when="midnight",
            interval=1,
            backupCount=7,
            encoding="utf-8"
        )
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
