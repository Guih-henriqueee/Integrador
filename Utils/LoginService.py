import psycopg2
from Repository.DictionaryTables import (
    pedidos_aprovados,
    pedido_itens
)
from Helper.ConnectionDB import get_db_schema_info, get_conn  
from Utils.FixTables import *

def tabela_existe(conn, schema, table):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables
                WHERE table_schema = %s AND table_name = %s
            )
        """, (schema, table))
        return cur.fetchone()[0]

def obter_colunas(conn, schema, table):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_schema = %s AND table_name = %s
        """, (schema, table))
        return {row[0]: {"data_type": row[1], "nullable": row[2] == "YES"} for row in cur.fetchall()}

def validar_estrutura_tabela(conn, tabela_def):
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

    colunas_esperadas = tabela_def["columns"]

    diferenças = {
        "faltantes": [],
        "tipos_diferentes": {}
    }

    if not tabela_existe(conn, schema, table):
        msg = f"Tabela {schema}.{table} não existe."
        return {"ok": False, "diferenças": msg}

    colunas_atuais = obter_colunas(conn, schema, table)

    ok = True
    for col_name, col_info in colunas_esperadas.items():
        if col_name not in colunas_atuais:
            diferenças["faltantes"].append(col_name)
            ok = False
        else:
            tipo_esperado = col_info["data_type"].lower()
            tipo_atual = colunas_atuais[col_name]["data_type"].lower()
            if tipo_esperado not in tipo_atual:
                diferenças["tipos_diferentes"][col_name] = {
                    "esperado": tipo_esperado,
                    "atual": tipo_atual
                }
                ok = False

    return {"ok": ok, "diferenças": diferenças}

def validar_todas_tabelas(conn):
    tables_definitions = {
        "pedidos_aprovados": pedidos_aprovados,
        "pedido_itens": pedido_itens,
    }

    resultados = {}
    for table_key, tabela_def in tables_definitions.items():
        print(f"🔄 [POSTGRES] - Validando {tabela_def['schema']}.{tabela_def['table_name']}...")
        resultado = validar_estrutura_tabela(conn, tabela_def)
        if not resultado["ok"]:
            print(f"❗ Diferenças encontradas. Corrigindo estrutura da tabela {tabela_def['table_name']}...")
            corrigir_estrutura(conn, tabela_def, resultado["diferenças"])
        else:
            print(f"✅ Tabela {tabela_def['table_name']} está OK. Nenhuma alteração necessária.")
        resultados[tabela_def['table_name']] = resultado
    return resultados

if __name__ == "__main__":
    try:
        with get_conn() as conn:
            resultados = validar_todas_tabelas(conn)
            print("\n📋 [POSTGRES] - Resumo da Validação:")
            for tabela, resultado in resultados.items():
                status = "✅ OK" if resultado["ok"] else "❌ Problemas"
                print(f"🔄 [POSTGRES] - {tabela}: {status}")
                
                if not resultado["ok"]:
                    difs = resultado["diferenças"]
                    if isinstance(difs, dict):
                        if difs.get("faltantes"):
                            print("    ❌ Colunas faltantes:")
                            for col in difs["faltantes"]:
                                print(f"      - {col}")
                        if difs.get("tipos_diferentes"):
                            print("    ⚠️ Colunas com tipos diferentes:")
                            for col, tipos in difs["tipos_diferentes"].items():
                                print(f"      - {col}: esperado '{tipos['esperado']}', encontrado '{tipos['atual']}'")
                    else:
                        print(f"    ❌ {difs}")
    except Exception as e:
        print(f"❌ [POSTGRES] - Erro na validação: {e}")
