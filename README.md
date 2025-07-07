# 🚀 Projeto de Integração de Pedidos - Precode

## 📖 Descrição

Este projeto realiza a **integração de pedidos** provenientes de múltiplos painéis (marketplaces e canais diversos) para um banco de dados PostgreSQL.

Ele captura pedidos via API, valida e corrige a estrutura do banco, insere novos pedidos, atualiza pedidos pendentes e mantém logs detalhados de operações.

O sistema suporta múltiplos canais, como **Shopee** e **Mercado Livre**, adaptando o processamento conforme o canal.

---

## 🛠 Tecnologias Utilizadas

* Python 3.x
* PostgreSQL
* Bibliotecas Python:

  * `requests`
  * `psycopg2`
  * `concurrent.futures` (built-in)
* APIs REST para consumo dos dados dos pedidos

---

## 🎯 Funcionalidades Principais

* ✅ Validação e correção automática da estrutura do banco de dados (tabelas, colunas, tipos)
* ✅ Consumo assíncrono e paralelo de APIs de múltiplos painéis com controle de limite de requisições por minuto
* ✅ Construção dinâmica dos dados de pedidos e itens, com tratamento específico para canais (Shopee, Mercado Livre, etc.)
* ✅ Registro detalhado de logs de integração, sucesso, erro, duplicação e atualização
* ✅ Reconsulta periódica de pedidos com status pendentes para atualização de dados
* ✅ Consulta do último pedido integrado por painel para continuidade da integração
* ✅ Verificação da existência de pedido para evitar duplicações
* ✅ Inserção e atualização de pedidos e itens no banco, garantindo dados consistentes

---

## 📁 Estrutura do Projeto

```plaintext
/Dependences
/Helper
    /Logger
        Enum/
        LoggerFactory.py
        LogService.py
    ConnectionDB.py
    Settings.py
/Repository
    DictionaryTables.py
    /Queryes
        QueryCheckOrdersNew.py
        QueryCheckOrdersPending.py
        QueryCreateTableItemsByOrder.py
        QueryCreateTableOrders.py
        QueryInsertItemByOrder.py
        QueryInsertLog.py
        QueryInsertOrder.py
        QueryOrderExists.py
        QueryStartOrder.py
        QueryTableExist.py
        QueryTableLayout.py
        TriggerMail.py
/Services
    InsertOrder.py
    Integrador.py
    OrderStarter.py
    SignUpLog.py
    TriggerMail.py
    UpdateOrdersPending.py
    UpdateRoutine.py
    VerifyTables.py
/Utils
    Builders.py
    EmailSender.py
    ExtractData.py
    FixTables.py
    LoginService.py
    QuoteSchema.py
/.env
/.gitignore
/main.py
/requirements.txt
/logs
```

---

## 🚀 Como Rodar

1. **Configure as variáveis de ambiente** e arquivo de configurações (`Helper.Settings.py`) com as informações de conexão, tokens e endpoints das APIs.

2. **Certifique-se que o banco PostgreSQL está disponível** e acessível.

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Execute o script principal**:

```bash
python main.py
```

> O sistema irá validar a estrutura do banco e iniciar as rotinas paralelas de integração e atualização.

---

## 📦 Dependências

* `requests`
* `psycopg2`
* `concurrent.futures` (parte da biblioteca padrão do Python)

---

## 👤 Autor

**Guilherme Martins**


