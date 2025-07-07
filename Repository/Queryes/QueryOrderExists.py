ORDER_EXIST = """
    SELECT 
        id
    FROM {SCHEMA}.{TABLE}
    WHERE 
        painel = %s and id = %s 
    LIMIT 1;
"""
