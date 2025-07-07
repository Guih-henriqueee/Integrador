pedido_itens = {
    "schema": "SANDBOX",
    "table_name": "pedido_itens",
    "columns": {
        "id": {
            "data_type": "serial4",
            "nullable": False,
            "primary_key": True
        },
        "pedido_id": {
            "data_type": "int8",
            "nullable": False,
            "foreign_key": {
                "schema": "SANDBOX",
                "table": "pedido_itens",
                "column": "id",
                "on_delete": "CASCADE"
            }
        },
        "sku": {
            "data_type": "int8",
            "nullable": True
        },
        "referencia_loja": {
            "data_type": "varchar",
            "length": 50,
            "nullable": True
        },
        "descricao_produto": {
            "data_type": "varchar",
            "length": 255,
            "nullable": True
        },
        "descricao_opcao": {
            "data_type": "varchar",
            "length": 100,
            "nullable": True
        },
        "valor_unitario": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "valor_unitario_liquido": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "quantidade": {
            "data_type": "int8",
            "nullable": True
        },
        "ncm": {
            "data_type": "varchar",
            "length": 20,
            "nullable": True
        },
        "volumes_unitario": {
            "data_type": "varchar",
            "length": 10,
            "nullable": True
        },
        "peso_unitario": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 3,
            "nullable": True
        },
        "gradex": {
            "data_type": "int8",
            "nullable": True
        },
        "gradey": {
            "data_type": "int8",
            "nullable": True
        },
        "tipo": {
            "data_type": "varchar",
            "length": 50,
            "nullable": True
        },
        "criado_em": {
            "data_type": "timestamp",
            "nullable": True,
            "default": "CURRENT_TIMESTAMP"
        },
        "atualizado_em": {
            "data_type": "timestamp",
            "nullable": True,
            "default": "CURRENT_TIMESTAMP"
        },
        "painel": {
            "data_type": "varchar",
            "nullable": True
        },

    },
    "primary_key": [
        "id"
    ],
    "indexes": [
        {
            "name": "idx_pedido_id",
            "columns": [
                "pedido_id"
            ]
        },
        {
            "name": "idx_sku",
            "columns": [
                "sku"
            ]
        },
    ],
    "foreign_keys": [
        {
            "column": "pedido_id",
            "references": {
                "schema": "SANDBOX",
                "table": "pedido_itens",
                "column": "id"
            },
            "on_delete": "CASCADE"
        },
    ],
}

pedidos_aprovados = {
    "schema": "SANDBOX",
    "table_name": "pedidos_aprovados",
    "columns": {
        "id": {
            "data_type": "int8",
            "nullable": False,
            "primary_key_part": True
        },
        "pedido_parceiro": {
            "data_type": "varchar",
            "length": 50,
            "nullable": True
        },
        "status": {
            "data_type": "varchar",
            "length": 30,
            "nullable": True
        },
        "id_status": {
            "data_type": "int8",
            "nullable": True
        },
        "data_inclusao": {
            "data_type": "timestamp",
            "nullable": True
        },
        "data_aprovacao": {
            "data_type": "timestamp",
            "nullable": True
        },
        "data_cancelamento": {
            "data_type": "timestamp",
            "nullable": True
        },
        "data_prevista_entrega": {
            "data_type": "date",
            "nullable": True
        },
        "canal": {
            "data_type": "varchar",
            "nullable": True
        },
        "valor_total": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "valor_frete": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "valor_desconto": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "cpf_cliente": {
            "data_type": "varchar",
            "length": 20,
            "nullable": True
        },
        "nome_cliente": {
            "data_type": "varchar",
            "length": 100,
            "nullable": True
        },
        "email_cliente": {
            "data_type": "varchar",
            "length": 150,
            "nullable": True
        },
        "uf": {
            "data_type": "varchar",
            "length": 2,
            "nullable": True
        },
        "cidade": {
            "data_type": "varchar",
            "length": 100,
            "nullable": True
        },
        "cep": {
            "data_type": "varchar",
            "length": 10,
            "nullable": True
        },
        "transportadora": {
            "data_type": "varchar",
            "length": 100,
            "nullable": True
        },
        "cnpj_transportadora": {
            "data_type": "varchar",
            "length": 20,
            "nullable": True
        },
        "url_rastreio": {
            "data_type": "text",
            "nullable": True
        },
        "itens": {
            "data_type": "jsonb",
            "nullable": True
        },
        "pagamentos": {
            "data_type": "jsonb",
            "nullable": True
        },
        "criado_em": {
            "data_type": "timestamp",
            "nullable": True,
            "default": "CURRENT_TIMESTAMP"
        },
        "atualizado_em": {
            "data_type": "timestamp",
            "nullable": True,
            "default": "CURRENT_TIMESTAMP"
        },
        "Parcelas": {
            "data_type": "varchar",
            "length": 1,
            "nullable": True
        },
        "QuantidadeParcelas": {
            "data_type": "int8",
            "nullable": True
        },
        "idAfiliado": {
            "data_type": "int8",
            "nullable": True
        },
        "Adquirente": {
            "data_type": "varchar",
            "length": 30,
            "nullable": True
        },
        "Frete_Seller": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "Frete_MercadoLivre": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "Carrinho_MercadoLivre": {
            "data_type": "varchar",
            "length": 50,
            "nullable": True
        },
        "ComissaoMercadoLivre": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "PercentualMercadoLivre": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "ComissaoShopee": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "ServicoShopee": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "MoedasShopee": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "VoucherShopee": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "DescontoShopee": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "DescontoFreteShopee": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "painel": {
            "data_type": "varchar",
            "nullable": True
        },
        "tipoPedido": {
            "data_type": "varchar",
            "length": 30,
            "nullable": True
        },
        "valorTotalDesconto": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complementoShopee_descontoFrete": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        
        "complementoShopee_voucher": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complementoShopee_comissao": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complementoShopee_taxaServico": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complementoShopee_moedas": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complementoShopee_shopeeDesconto": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complementoMeli_comissaoTotal": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complementoMeli_comissaoPercentual": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complemento_DescontoObs": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "complemento_canalVenda": {
            "data_type": "varchar",
            "length": 30,
            "nullable": True
        
        },

        "complemento_valorComissao": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "FretePagoSeller": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        "Frete_TotalMercadoLivre": {
            "data_type": "numeric",
            "precision": 12,
            "scale": 2,
            "nullable": True
        },
        
        
    },
    "primary_key": [
        "id",
        "painel"
    ],
    "indexes": [
        {
            "name": "idx_canal",
            "columns": [
                "canal"
            ]
        },
        {
            "name": "idx_data_aprovacao",
            "columns": [
                "data_aprovacao"
            ]
        },
        {
            "name": "idx_status_aprovado",
            "columns": [
                "status"
            ]
        },
    ],

}