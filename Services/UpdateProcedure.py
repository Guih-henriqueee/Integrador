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


def Update_Procedure_PEDIDOS(conn):
    query = 'CALL "ODS".PROC_ODS_PEDIDOS_PRECODE();'
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except Exception as e:
        print(f"⚠️ [PROCEDURE] - Falha ao executar PROC_ODS_PEDIDOS_PRECODE: {e}")
        return False
    return True


def Update_Procedure_CAMPANHAS(conn, dt_ini: str, dt_fim: str):
    query = f'CALL "DW".PROC_DW_PEDIDOS_CAMPANHAS(\'{dt_ini}\'::DATE, \'{dt_fim}\'::DATE);'
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except Exception as e:
        print(f"⚠️ [PROCEDURE] - Falha ao executar PROC_DW_PEDIDOS_CAMPANHAS: {e}")
        return False
    return True
