INSERT_ORDER = """
    INSERT INTO {SCHEMA}.{TABLE} (
        id,
        pedido_parceiro,
        status,
        data_aprovacao,
        data_prevista_entrega,
        canal,
        valor_total,
        valor_frete,
        valor_desconto,
        cpf_cliente,
        nome_cliente,
        email_cliente,
        uf,
        cidade,
        cep,
        transportadora,
        cnpj_transportadora,
        url_rastreio,
        itens,
        pagamentos,
        painel
    ) VALUES (
        %(id)s,
        %(pedido_parceiro)s,
        %(status)s,
        %(data_aprovacao)s,
        %(data_prevista_entrega)s,
        %(canal)s,
        %(valor_total)s,
        %(valor_frete)s,
        %(valor_desconto)s,
        %(cpf_cliente)s,
        %(nome_cliente)s,
        %(email_cliente)s,
        %(uf)s,
        %(cidade)s,
        %(cep)s,
        %(transportadora)s,
        %(cnpj_transportadora)s,
        %(url_rastreio)s,
        %(itens)s,
        %(pagamentos)s,
        %(painel)s
    )
    ON CONFLICT (id, painel) DO NOTHING;
"""
