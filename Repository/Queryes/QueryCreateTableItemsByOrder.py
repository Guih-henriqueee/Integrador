CREATE_TABLE_ITEMS_BY_ORDER = """

			CREATE TABLE {SCHEMA}.pedido_itens (
				id 															serial4 								NOT NULL,
				pedido_id 													int8 									NOT NULL,
				sku 														int4 									NULL,
				referencia_loja 											varchar(50) 							NULL,
				descricao_produto											varchar(255) 							NULL,
				descricao_opcao 											varchar(100) 							NULL,
				valor_unitario 												numeric(12, 2) 							NULL,
				valor_unitario_liquido 										numeric(12, 2) 							NULL,
				quantidade 													int4 									NULL,
				ncm 														varchar(20) 							NULL,
				volumes_unitario 											varchar(10) 							NULL,
				peso_unitario 												numeric(12, 3) 							NULL,
				gradex 														int4 									NULL,
				gradey 														int4 									NULL,
				tipo 														varchar(50) 							NULL,
				criado_em 													timestamp DEFAULT CURRENT_TIMESTAMP 	NULL,
				painel 														varchar 								NULL,
				
    
    			CONSTRAINT pedido_itens_pkey PRIMARY KEY (id),
				CONSTRAINT fk_pedido FOREIGN KEY (pedido_id) REFERENCES {SCHEMA}.pedido_itens(id) ON DELETE CASCADE
			);
			CREATE INDEX idx_pedido_id 				ON {SCHEMA}.pedido_itens USING btree (pedido_id);
			CREATE INDEX idx_sku 					ON {SCHEMA}.pedido_itens USING btree (sku);


"""


# ===================================== PENDENTE MONTAR LAYOUT =====================================
# 
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
# Shopee									 Precode	[SP]				  		[	X	]       |
# Banco Inter								 Precode	[SP]								 		|
# Bradesco									 Precode	[SP]								 		|
# AliExpress								 Precode	[MG]								 		|
# TikTok									 Precode	[MG]								 		|
# ===================================== 	 MARKETPLACES      =====================================