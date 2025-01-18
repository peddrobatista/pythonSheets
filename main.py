from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Define os escopos necessários para acessar a API do Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# ID e intervalo da planilha
SAMPLE_SPREADSHEET_ID = "1ns87fsrOGXw755udA-nL9L4X8awcU606IafyG1UJBDg"
SAMPLE_RANGE_NAME = "Página1!A1:G18"

# Caminho para o arquivo de credenciais da conta de serviço
SERVICE_ACCOUNT_FILE = "credentials.json"


def main():
    # Autentica com as credenciais da conta de serviço
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        # Constrói o serviço para acessar a API do Google Sheets
        service = build("sheets", "v4", credentials=creds)

        # Chamando a API do Google Sheets para buscar os dados

        # lendo os dados
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        
        values = result.get("values", [])

        if not values:
            print("Nenhum dado encontrado.")
            return

        # Imprime os dados retornados da planilha
        # print(result)
        print("Dados encontrados:")
        for row in values:
            print(row)

        # adicionando / editando os dados
        # valores_adicionar = [['Pedro','', 1300], ['Maria']]
        # result = (
        #     sheet.values()
        #     .update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="B17", 
        #             valueInputOption="USER_ENTERED",
        #             body={'values': valores_adicionar})
        #     .execute()
        # )

        # adicionando uma nova coluna com novos valores
        valores_adicionar = [
            ['Aumento'],
        ]
        for i, linha in enumerate(values):
            if i > 0:
                salario = linha[3]
                salario = salario.replace("R$ ", "").replace(".", "")
                salario = float(salario.replace(",", "."))
                aumento = salario * 0.1
                valores_adicionar.append([aumento])
        result = (
            sheet.values()
            .update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="G1", 
                     valueInputOption="USER_ENTERED",
                     body={'values': valores_adicionar})
             .execute()
        )

    except Exception as err:
        print(f"Erro ao acessar a API do Google Sheets: {err}")


if __name__ == "__main__":
    main()
