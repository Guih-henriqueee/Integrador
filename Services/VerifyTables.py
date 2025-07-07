import psycopg2
from Helper.Settings import LoadSettingsOnEnv
from Helper.ConnectionDB import get_conn, get_db_schema_info
from Repository.Queryes.QueryTableExist import EXIST_TABLE
from Repository.Queryes.QueryTableLayout import LAYOUT_TABLE
from Utils.QuoteSchema import quoted

DB_CONFIG = LoadSettingsOnEnv()
schema, table, _, _ = get_db_schema_info()
schema = schema.upper()

def tabela_existe(conn, schema: str, tabela: str) -> bool:
    with conn.cursor() as cur:
        cur.execute(EXIST_TABLE, (quoted(schema), tabela))
        resultado = cur.fetchone()
        return bool(resultado[0]) if resultado else False

def check_in_tables(conn, schema: str, tabela: str):
    with conn.cursor() as cur:
        cur.execute(LAYOUT_TABLE, (quoted(schema), tabela))
        resultado = cur.fetchone()
        return resultado if resultado else None
