ORDERS_PENDING = """
            SELECT 
                id,
                painel, 
                data_inclusao,
                valor_total 
            FROM {SCHEMA}.{TABLE}
            WHERE id_status IN (1)
            ORDER BY criado_em DESC
"""