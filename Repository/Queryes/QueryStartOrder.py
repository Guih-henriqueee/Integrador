ORDER_START = """
    SELECT 
        id
    FROM {SCHEMA}.{TABLE}
    WHERE 
        painel = %s 
    ORDER BY 1 DESC
    LIMIT 1;
"""
