CREATE_TABLE_ORDERS = """
			CREATE TABLE {SCHEMA}.{TABLE} (
				id 													INT8 										NOT NULL,
				pedido_parceiro 									VARCHAR(50) 								NULL,
				status 												VARCHAR(30) 								NULL,
				id_status											INT8		 								NULL,
				data_inclusao 										TIMESTAMP 									NULL,
				data_aprovacao 										TIMESTAMP 									NULL,
				data_cancelamento 									TIMESTAMP 									NULL,
				data_prevista_entrega 								DATE 										NULL,
				canal 												VARCHAR										NULL,
				valor_total 										NUMERIC(12, 2) 								NULL,
				valor_frete 										NUMERIC(12, 2) 								NULL,
				valor_desconto 										NUMERIC(12, 2) 								NULL,
				cpf_cliente 										VARCHAR(20) 								NULL,
				nome_cliente 										VARCHAR(100) 								NULL,
				email_cliente 										VARCHAR(150) 								NULL,
				uf 													VARCHAR(2) 									NULL,
				cidade 												VARCHAR(100) 								NULL,
				cep 												VARCHAR(10) 								NULL,
				transportadora 										VARCHAR(100) 								NULL,
				cnpj_transportadora 								VARCHAR(20) 								NULL,
				url_rastreio 										TEXT 										NULL,
				itens 												JSONB 										NULL,
				pagamentos 											JSONB 										NULL,
				criado_em 											TIMESTAMP DEFAULT CURRENT_TIMESTAMP 		NULL,
				parcelas											VARCHAR(1)									NOT NULL,
				quantidadeParcelas									INT8										NULL,
				adquirente											VARCHAR(30)									NULL,
				frete_Seller										NUMERIC(12, 2)								NULL,
				frete_mercadolivre									NUMERIC(12, 2)								NULL,
				carrinho_mercadolivre								VARCHAR(50)									NULL,
				comissao_mercadolivre								NUMERIC(12, 2)								NULL,
				percentual_mercadolivre								NUMERIC(12, 2)								NULL,
				comissao_shopee										NUMERIC(12, 2)								NULL,
				servico_shopee										NUMERIC(12, 2)								NULL,
				servico_shopee										NUMERIC(12, 2)								NULL,
				moedas_shopee										NUMERIC(12, 2)								NULL,
				voucher_shopee										NUMERIC(12, 2)								NULL,
				desconto_shopee										NUMERIC(12, 2)								NULL,
				descontofrete_shopee								NUMERIC(12, 2)								NULL,
				painel 												VARCHAR 									NULL,
				
    
    			CONSTRAINT 											{TABLE}_pkey 						PRIMARY KEY (id, painel)
			);
   
			CREATE INDEX idx_canal 					ON "SANDBOX".{TABLE} USING btree (canal);
			CREATE INDEX idx_data_aprovacao 		ON "SANDBOX".{TABLE} USING btree (data_aprovacao);
			CREATE INDEX idx_status_aprovado 		ON "SANDBOX".{TABLE} USING btree (status);


"""

# Incluido coluna 'data_aprovacao'
# Incluido coluna 'data_criacao'
# Incluido coluna 'data_cancelamento'
# Incluido coluna 'id_status'
# Incluido coluna 'Parcelas'																		
# Incluido coluna 'QuantidadeParcelas'									
# Incluido coluna 'dquirente'											,
# Incluido coluna 'frete_Seller'				
# Incluido coluna 'frete_mercadolivre'
# Incluido coluna 'Carrinho_mercadolivre'
# Incluido coluna 'Comissaomercadolivre'
# Incluido coluna 'Percentualmercadolivre'
# Incluido coluna 'Comissao_shopee'
# Incluido coluna 'Servico_shopee'
# Incluido coluna 'Servico_shopee'
# Incluido coluna 'Moedas_shopee'
# Incluido coluna 'Voucher_shopee'
# Incluido coluna 'Desconto_shopee'
# Incluido coluna 'Descontofrete_shopee'

# ===================================== PENDENTE MONTAR LAYOUT =====================================
# CAMPOS MERCADO LIVRE
# fRETE PAGO SELLER
# fRETE TOTAL MERCADO LIVRE
# CÓDIGO CARRINHO DE COMPRAS
# COMISSAO TOTAL
# COMISSAO PERCENTUAL
# TIPO ANUNCIO
# TRADICIONAL/BUYBOX - CLASSICO/PREMIUM 

# CAMPOS _sHOPEE
# COMISSAO
# TAXA SERVICO
# MOEDAS
# _sHOPEE DESCONTO
# VOUCHER
# DESCONTO fRETE
# ===================================== PENDENTE MONTAR LAYOUT =====================================
# ===================================== 	 MARKETPLACES      =====================================
# 				CANAL 							  HUB							ESTRUTURA MAPEADA	|
# Mercado Livre SP							 Precode	[SP]				  		[	X	]		|
# Mercado Livre MG							 Precode	[MG]				  		[	X	]		|
# Mercado Shops								 Precode	[SP]				  		[	X	]		|
# Americanas S.A							 Precode	[MG]								 		|
# Magazine Luiza SP							 Precode	[SP]								 		|			
# Amazon SP									 Precode	[SP]								 		|
# Kabum SP									 Precode	[SP]								 		|
# _shopee									 Precode	[SP]				  		[	X	]       |
# Banco Inter								 Precode	[SP]								 		|
# Bradesco									 Precode	[SP]								 		|
# AliExpress								 Precode	[MG]								 		|
# TikTok									 Precode	[MG]								 		|
# ===================================== 	 MARKETPLACES      =====================================