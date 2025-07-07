import psycopg2
from Helper.Settings import LoadSettingsOnEnv
from Helper.ConnectionDB import get_conn, get_db_schema_info
from Repository.Queryes.QueryInsertLog import INSERT_LOG
from Utils.QuoteSchema import quoted


def registrar_log(conn, pedido_id, status, painel, mensagem=""):
    schema, _, _, table = get_db_schema_info()
    schema = schema.upper()
    query = INSERT_LOG.format(SCHEMA=quoted(schema), TABLE=table)
    with conn.cursor() as cur:
        cur.execute(query, (pedido_id, status, painel, mensagem))
