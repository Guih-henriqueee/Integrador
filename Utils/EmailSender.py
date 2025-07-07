import smtplib
import tempfile
import os
import pandas as pd
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def calcular_dias_pendentes(data_pedido):
    hoje = datetime.now()
    if not data_pedido:
        return "N/A"
    return (hoje - data_pedido).days

def gerar_tabela_html_pedidos(pedidos):
    linhas = ""
    for pedido_id, painel, data_pedido in pedidos:
        dias_pendentes = calcular_dias_pendentes(data_pedido)
        linhas += f"""
        <tr>
            <td>{pedido_id}</td>
            <td>{painel}</td>
            <td>{dias_pendentes}</td>
        </tr>
        """
    tabela = f"""
    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
        <thead>
            <tr>
                <th>Pedido</th>
                <th>Painel</th>
                <th>Dias Pendentes</th>
            </tr>
        </thead>
        <tbody>
            {linhas}
        </tbody>
    </table>
    """
    return tabela

def gerar_excel_temp(pedidos):
    dados = []
    for pedido_id, painel, data_pedido in pedidos:
        dados.append({
            "Pedido": pedido_id,
            "Painel": painel,
            "Data Pedido": data_pedido.strftime("%d/%m/%Y") if data_pedido else "N/A",
            "Dias Pendentes": calcular_dias_pendentes(data_pedido)
        })

    df = pd.DataFrame(dados)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    df.to_excel(temp_file.name, index=False)
    return temp_file.name

def enviar_email_pedidos_pendentes(pedidos, remetente, senha, destinatario):
    msg = MIMEMultipart('mixed')
    msg['Subject'] = "📦 Pedidos Pendentes de Atualização"
    msg['From'] = remetente
    msg['To'] = destinatario

    html_part = MIMEMultipart('alternative')
    corpo_html = f"""
    <html>
        <body>
            <p>Olá,</p>
            <p>Segue a relação dos pedidos pendentes e a quantidade de dias:</p>
            {gerar_tabela_html_pedidos(pedidos)}
            <p>O mesmo conteúdo está disponível em anexo no formato Excel (.xlsx).</p>
            <p>Att,<br/>Sistema de Integração</p>
        </body>
    </html>
    """
    html_part.attach(MIMEText(corpo_html, 'html'))
    msg.attach(html_part)

    excel_path = gerar_excel_temp(pedidos)
    with open(excel_path, "rb") as f:
        part = MIMEApplication(f.read(), Name="PedidosPendentes.xlsx")
        part['Content-Disposition'] = 'attachment; filename="PedidosPendentes.xlsx"'
        msg.attach(part)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario, msg.as_string())
        print("📧 Email com Excel enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")
    finally:
        os.remove(excel_path) 