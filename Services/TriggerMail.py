import psycopg2
from Helper.ConnectionDB import get_conn, get_db_schema_info
from Repository.Queryes.QueryCheckOrdersPending import ORDERS_PENDING  
from Utils.QuoteSchema import quoted
from Utils.EmailSender import enviar_email_pedidos_pendentes

REMETENTE = "seuemail@dominio.com"
SENHA = "sua_senha_de_app"  
DESTINATARIO = "destinatario@dominio.com"

schema_config, table_orders, *_ = get_db_schema_info()
schema_config = quoted(schema_config)

with get_conn() as conn:
    cur = conn.cursor()
    try:
        query = ORDERS_PENDING.format(SCHEMA=schema_config, TABLE=table_orders)
        cur.execute(query)
        pedidos_pendentes = cur.fetchall()
        print(f"🔍 {len(pedidos_pendentes)} pedidos pendentes encontrados.")
    except Exception as e:
        print(f"❌ [MAILSENDER] - Erro ao consultar pedidos pendentes: {e}")
        pedidos_pendentes = []

if pedidos_pendentes:
    enviar_email_pedidos_pendentes(pedidos_pendentes, REMETENTE, SENHA, DESTINATARIO)
else:
    print("✅ Nenhum pedido pendente. Email não enviado.")
