import json
from Utils.ExtractData import extrair_data_aprovacao, extrair_data_cancelamento, extrair_data_novo

def Builder_Base(pedido, codigoPedido, painel):
    data_aprovacao = extrair_data_aprovacao(pedido)
    data_inclusao = extrair_data_novo(pedido)
    data_cancelment = extrair_data_cancelamento(pedido)
    
    pagamento_lista = pedido.get("pagamento", [])
    pagamento_info = pagamento_lista[0] if isinstance(pagamento_lista, list) and pagamento_lista else {}

    quantidade_parcelas = pagamento_info.get("quantidadeParcelas")
    parcelas = pagamento_info.get("quantidadeParcelas")
    adquirente = pagamento_info.get("adquirente")

    try:
        parcelas = int(parcelas)
        parcelas = 'Y' if parcelas > 1 else 'N'
    except (TypeError, ValueError):
        parcelas = None
        
        
    return {
        "id": codigoPedido,
        "pedido_parceiro": pedido.get("pedidoParceiro"),
        "tipoPedido": pedido.get("tipoPedido"),
        "status": pedido.get("statusAtual"),
        "data_aprovacao": data_aprovacao,
        "data_inclusao": data_inclusao,
        "data_cancelamento": data_cancelment,
        "data_prevista_entrega": pedido.get("previsaoEntrega"),
        "canal": pedido.get("nomeAfiliado"),
        "valor_total": pedido.get("valorTotalCompra"),
        "valor_frete": pedido.get("valorFrete"),
        "valor_desconto": pedido.get("valorTotalDesconto"),
        "cpf_cliente": pedido.get("dadosCliente", {}).get("cpfCnpj"),
        "nome_cliente": pedido.get("dadosCliente", {}).get("nomeRazao"),
        "email_cliente": pedido.get("dadosCliente", {}).get("email"),
        "uf": pedido.get("dadosCliente", {}).get("dadosEntrega", {}).get("uf"),
        "cidade": pedido.get("dadosCliente", {}).get("dadosEntrega", {}).get("cidade"),
        "cep": pedido.get("dadosCliente", {}).get("dadosEntrega", {}).get("cep"),
        "transportadora": pedido.get("dadosRastreio", {}).get("transportadora"),
        "cnpj_transportadora": pedido.get("dadosRastreio", {}).get("CNPJtransportadora"),
        "url_rastreio": pedido.get("dadosRastreio", {}).get("urlRastreio"),
        "itens": json.dumps(pedido.get("itens", [])),
        "pagamentos": json.dumps(pedido.get("pagamento", [])),
        "valorTotalDesconto": pedido.get("valorTotalDesconto"),
        "idAfiliado": pedido.get("idAfiliado"),
        "painel": painel,
        "complemento_DescontoObs": pedido.get("complemento", {}).get("DescontoObs"),
        "complemento_canalVenda": pedido.get("complemento", {}).get("canalVenda"),
        "complemento_valorComissao": pedido.get("complemento", {}).get("valorComissao"),
        "id_status": pedido.get("codigoStatusAtual"),   
        "Parcelas": parcelas,
        "QuantidadeParcelas": quantidade_parcelas,   
        "Adquirente": adquirente,
    }

def Builder_Shopee(pedido, codigoPedido, painel):
    base = Builder_Base(pedido, codigoPedido, painel)
    base.update({
        "ComissaoShopee": pedido.get("complementoShopee", {}).get("comissao"),
        "ServicoShopee": pedido.get("complementoShopee", {}).get("taxaServico"),
        "MoedasShopee": pedido.get("complementoShopee", {}).get("moedas"),
        "DescontoShopee": pedido.get("complementoShopee", {}).get("shopeeDesconto"),
        "VoucherShopee": pedido.get("complementoShopee", {}).get("voucher"),
        "DescontoFreteShopee": pedido.get("complementoShopee", {}).get("descontoFrete"),
    })
    return base

def Builder_MercadoLivre(pedido, codigoPedido, painel):
    base = Builder_Base(pedido, codigoPedido, painel)
    base.update({
        "ComissaoMercadoLivre": pedido.get("complementoMeli", {}).get("comissaoTotal"),
        "PercentualMercadoLivre": pedido.get("complementoMeli", {}).get("comissaoPercentual"),
        "Frete_MercadoLivre": pedido.get("FreteTotalMercadoLivre"),
        "Carrinho_MercadoLivre": pedido.get("codigoCarrinhoCompras"),
        "Frete_Seller": pedido.get("FretePagoSeller")
    })
    return base


def Builder_Items(pedido, codigoPedido, painel):
    base_items = []
    itens = pedido.get("itens", [])
    
    for item in itens:
        base_item = {
            "pedido_id": codigoPedido,
            "sku": item.get("sku"),
            "referencia_loja": item.get("referenciaLoja") or item.get("referencia"),
            "descricao_produto": item.get("descricaoProduto") or item.get("descricao"),
            "descricao_opcao": item.get("descricaoOpcao") or item.get("opcao"),
            "valor_unitario": item.get("valorUnitario"),
            "valor_unitario_liquido": item.get("valorUnitarioLiquido"),
            "quantidade": item.get("quantidade"),
            "ncm": item.get("ncm"),
            "volumes_unitario": item.get("volumesUnitario"),
            "peso_unitario": item.get("pesoUnitario"),
            "gradex": item.get("gradex"),
            "gradey": item.get("gradey"),
            "tipo": item.get("tipo"),
            "painel": painel
        }
        base_items.append(base_item)
    
    return base_items