# -*- coding: utf-8 -*-
from datetime import datetime

def extrair_data_aprovacao(pedido):
    for evento in pedido.get("dadosAcompanhamento", []):
        if evento["descricao"].lower() == "aprovado":
            data_str = f"{evento['data']} {evento['hora']}"
            return datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
    return None

def extrair_data_novo(pedido):
    for evento in pedido.get("dadosAcompanhamento", []):
        if evento["descricao"].lower() == "novo":
            data_str = f"{evento['data']} {evento['hora']}"
            return datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
    return None

def extrair_data_cancelamento(pedido):
    for evento in pedido.get("dadosAcompanhamento", []):
        if evento["descricao"].lower() == "cancelado":
            data_str = f"{evento['data']} {evento['hora']}"
            return datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
    return None
