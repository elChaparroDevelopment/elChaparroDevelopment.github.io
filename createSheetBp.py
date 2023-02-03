import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date


scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("backend/data/elchaparrobackend-d967ddb3c7ea.json", scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("SalesElChaparro")
sheet = workbook.sheet1

def createSheet(place):
    # Getting all data I need
    today = date.today()
    sheetName = str(str(place) + ':' + str(today))
    sheetindx = int(sheet.acell('B2').value) + 1

    # Creating Worksheet
    # worksheet = workbook.add_worksheet(title=sheetName, rows="100", cols="20")

    # Update Db
    CurrSheet = workbook.get_worksheet(sheetindx)
    sheet.update_acell('B2', sheetindx)
    sheet.update('B1', 2)

    # Set Basic Sheet
    CurrSheet.update('A1:K1',[['SaleId','Hombre','Mujer','Birria','Carne Asada','Pollo','Gaseosa','DateTime','Total']])

def addRow(data):
    # Getting data I need
    currRow = sheet.acell('B1').value
    return (data + " and current row is: " + currRow)
