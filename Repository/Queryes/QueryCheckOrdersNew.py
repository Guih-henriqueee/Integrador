ORDERS_NEW = """
            SELECT 
                id,
                painel 
            FROM {SCHEMA}.{TABLE}
            WHERE id_status IN (1)
            ORDER BY criado_em DESC
"""