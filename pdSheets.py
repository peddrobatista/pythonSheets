import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Caminho para o arquivo de credenciais da conta de serviço
credentials = "credentials.json"

# Escopos necessários para acessar a API do Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# Autenticação com as credenciais da conta de serviço
creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename=credentials, scopes=scopes
)
client = gspread.authorize(creds)

# Acessa a planilha pelo ID
SHEET_ID = "1ns87fsrOGXw755udA-nL9L4X8awcU606IafyG1UJBDg"
planilha = client.open_by_key(SHEET_ID)

# Seleciona a primeira aba da planilha
planilhafull = planilha.get_worksheet(0)

# Obtém todos os registros da aba
dados = planilhafull.get_all_records()

# Exibe os dados no console
def mostrarPlanilha(planilha):
    dados = planilha.get_all_records()
    df = pd.DataFrame(dados)
    print(df)

# READ
mostrarPlanilha(planilhafull)

# CREATE
planilhafull.update_cell(row=19, col=1, value=18)
mostrarPlanilha(planilhafull)

# UPDATE
planilhafull.update_acell(label='B18', value="Mary")
mostrarPlanilha(planilhafull)

# DELETE
planilhafull.delete_rows(18)
mostrarPlanilha(planilhafull)
