INSERT_ITEM_BY_ORDER = """
    INSERT INTO {SCHEMA}.{TABLE} (
        pedido_id,
        sku,
        referencia_loja,
        descricao_produto,
        descricao_opcao,
        valor_unitario,
        valor_unitario_liquido,
        quantidade,
        ncm,
        volumes_unitario,
        peso_unitario,
        gradex,
        gradey,
        tipo
    ) VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    );
"""