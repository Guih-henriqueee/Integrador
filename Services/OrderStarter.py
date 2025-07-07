from Repository.Queryes.QueryStartOrder import ORDER_START
from Repository.Queryes.QueryOrderExists import ORDER_EXIST
from Helper.ConnectionDB import get_db_schema_info
from Utils.QuoteSchema  import quoted

schema_config, table_orders, table_items, table_logs = get_db_schema_info()
schema_quoted = schema_config.upper()


query_order_start = ORDER_START.format(
    SCHEMA=quoted(schema_quoted),
    TABLE=table_orders
)

query_order_exist = ORDER_EXIST.format(
    SCHEMA=quoted(schema_quoted),
    TABLE=table_orders
)

def buscar_ultimo_id_por_painel(conn, painel):
    with conn.cursor() as cur:
        cur.execute(query_order_start, (painel,))
        resultado = cur.fetchone()
        if resultado:
            return {"id": resultado[0]}
        
        return None


def verifica_pedido(conn, painel, pedido):
    with conn.cursor() as cur:
        cur.execute(query_order_exist, (painel, pedido,))
        resultado = cur.fetchone()
        if resultado:
            return {"id": resultado[0], "painel": resultado[1]}
        return None
