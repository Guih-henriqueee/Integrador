#config.py
# -*- coding: utf-8 -*-
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def to_int(value, default):
    try:
        return int(value)
    except:
        return default

lista_vazia = to_int(os.getenv("TEMPO_ESPERA_LISTA_VAZIA"), 15) * 60

def LoadSettingsOnEnv():
    Settings = []
    i = 1
    while True:
        base_url = os.getenv(f"API_BASE_URL_{i}")
        token = os.getenv(f"API_TOKEN_{i}")
        rate_limit = os.getenv(f"API_RATE_LIMIT_{i}")
        start_order = os.getenv(f"API_START_ORDER_{i}")
        end_order = os.getenv(f"API_END_ORDER_{i}")
        painel = os.getenv(f"API_{i}")
        if not base_url or not token:
            break
        Settings.append({
            "base_url": base_url,
            "token": token,
            "painel": painel,
            "limite_por_minuto": to_int(rate_limit, 30),
            "start_order": int(start_order) if start_order and start_order.isdigit() else None,
            "end_order": int(end_order) if end_order and end_order.isdigit() else None,
            "lista_vazia": lista_vazia
        })
        i += 1
    return Settings

API_CONFIGS = LoadSettingsOnEnv()

def LoadSettingsOnDB():
    DB_CONFIG = {
        "host": os.getenv("DB_HOST"),
        "port": to_int(os.getenv("DB_PORT"), 5432),
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }
    extras = {
        "schema": os.getenv("DB_SCHEMA"),
        "table_order": os.getenv("ORDERS"),
        "table_items": os.getenv("ITEMS_BY_ORDER"),
        "table_logs": os.getenv("LOGS_TABLE")
    }
    return DB_CONFIG, extras

def test_get_conn():
    DB_CONFIG, _ = LoadSettingsOnDB()
    return psycopg2.connect(**DB_CONFIG)