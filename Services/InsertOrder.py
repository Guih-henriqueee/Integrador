import psycopg2
from Helper.Settings import LoadSettingsOnEnv
from Helper.ConnectionDB import get_conn, get_db_schema_info
from Repository.Queryes.QueryInsertOrder import INSERT_ORDER
from Utils.QuoteSchema import quoted

DB_CONFIG = LoadSettingsOnEnv()
schema_config, table_orders, table_items, table_logs = get_db_schema_info()
schema_quoted = schema_config.upper()
schema_config = quoted(schema_config)

query_insert_order = INSERT_ORDER.format(SCHEMA=schema_config, TABLE=table_orders)


def inserir_pedido(conn, pedido):
    cols = pedido.keys()
    cols_quoted = [f'"{col}"' for col in cols]
    colunas_str = ", ".join(cols_quoted)
    placeholders = ", ".join(f"%({col})s" for col in cols)
    query = f"""
        INSERT INTO {schema_config}.{table_orders} ({colunas_str})
        VALUES ({placeholders})
    """
    
    with conn.cursor() as cur:
        cur.execute(query, pedido)

def atualizar_pedido(conn, pedido):
    cols = [col for col in pedido.keys() if col != "id"]
    set_str = ", ".join(f'"{col}" = %({col})s' for col in cols)
    query = f"""
        UPDATE {schema_config}.{table_orders}
        SET {set_str}
        WHERE id = %(id)s
    """
    
    with conn.cursor() as cur:
        cur.execute(query, pedido)


def inserir_itens(conn, pedido_id, itens):
    if not itens:
        return

    itens_com_id = []
    for item in itens:
        item_copy = item.copy()
        item_copy["pedido_id"] = pedido_id
        itens_com_id.append(item_copy)

    cols = itens_com_id[0].keys()
    colunas_str = ", ".join(cols)
    placeholders = ", ".join(f"%({col})s" for col in cols)

    query = f"""
        INSERT INTO {schema_config}.{table_items} ({colunas_str})
        VALUES ({placeholders})
    """

    with conn.cursor() as cur:
        cur.executemany(query, itens_com_id)
    conn.commit()

def atualizar_itens(conn, pedido_id, itens):
    if not itens:
        return

    with conn.cursor() as cur:
        cur.execute(f"DELETE FROM {schema_config}.{table_items} WHERE pedido_id = %s", (pedido_id,))
    
    inserir_itens(conn, pedido_id, itens)

