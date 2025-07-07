INSERT_LOG = """
    INSERT INTO {SCHEMA}.{TABLE} (
        pedido_id,
        status_integracao,
        mensagem,
        fonte
    ) VALUES (
        %s,
        %s,
        %s,
        %s);
"""
