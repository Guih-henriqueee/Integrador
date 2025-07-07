import time
from Helper.ConnectionDB import get_db_schema_info

def gerar_add_column_sql(schema, table, coluna, col_info):
    tipo = col_info["data_type"]
    nullable = col_info.get("nullable", True)
    null_str = "" if nullable else "NOT NULL"
    return f'ALTER TABLE "{schema}"."{table}" ADD COLUMN "{coluna}" {tipo} {null_str};'


def backup_tabela_simples(conn, schema, table):
    with conn.cursor() as cur:
        timestamp = int(time.time())
        tabela_backup = f"{table}_backup_{timestamp}"
        sql = f' - CREATE TABLE "{schema}"."{tabela_backup}" AS TABLE "{schema}"."{table}";'
        print(f"Fazendo backup da tabela {schema}.{table} para {schema}.{tabela_backup} ...")
        cur.execute(sql)
    conn.commit()

def gerar_alter_column_type_sql(schema, table, coluna, novo_tipo):
    if novo_tipo.lower() in ('serial4', 'serial'):
        novo_tipo_real = 'integer'
    elif novo_tipo.lower() == 'serial8':
        novo_tipo_real = 'bigint'
    else:
        novo_tipo_real = novo_tipo

    return f'ALTER TABLE "{schema}"."{table}" ALTER COLUMN "{coluna}" TYPE {novo_tipo_real} USING "{coluna}"::{novo_tipo_real};'


def corrigir_estrutura(conn, tabela_def, diferencas):
    schema_config, table_orders, table_items, table_logs = get_db_schema_info()

    table_name = tabela_def["table_name"]
    if table_name == "pedidos_aprovados":
        schema = schema_config
        table = table_orders
    elif table_name == "pedido_itens":
        schema = schema_config
        table = table_items
    else:
        schema = tabela_def["schema"]
        table = table_name

    with conn.cursor() as cur:
        for coluna in diferencas["faltantes"]:
            col_info = tabela_def["columns"][coluna]
            sql = gerar_add_column_sql(schema, table, coluna, col_info)
            print(f"🛠️  [POSTGRESS] - Executando SQL para adicionar coluna: {sql}")
            cur.execute(sql)

        for coluna, tipos in diferencas["tipos_diferentes"].items():
            novo_tipo = tipos["esperado"]
            sql = gerar_alter_column_type_sql(schema, table, coluna, novo_tipo)
            print(f"🛠️  [POSTGRESS] - Executando SQL para alterar tipo da coluna: {sql}")
            cur.execute(sql)

    conn.commit()
