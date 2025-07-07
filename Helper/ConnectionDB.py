import psycopg2
from Helper.Settings import LoadSettingsOnDB

def get_conn():
    DB_CONFIG, _ = LoadSettingsOnDB()
    return psycopg2.connect(**DB_CONFIG)

def get_db_schema_info():
    _, extras = LoadSettingsOnDB()

    return (
        extras.get("schema", "public"),
        extras.get("table_orders", "pedidos_aprovados"),
        extras.get("table_items_by_order", "pedido_itens"),
        extras.get("table_logs", "pedidos_log_integracao"),
             )