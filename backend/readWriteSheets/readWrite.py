import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request


scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("backend/data/elchaparrobackend-d967ddb3c7ea.json", scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("SalesElChaparro")
# workbook.duplicate_sheet("1QIUqKlWnsehZlh9Qe5lxw6q8ETJ5l7HTiOaChMPGaUU", new_sheet_name="TodayDate")
# accessgoogleapis@elchaparrobackend.iam.gserviceaccount.com
# file.copy("1QIUqKlWnsehZlh9Qe5lxw6q8ETJ5l7HTiOaChMPGaUU", title="timcard2", copy_permissions=True)
# worksheet = file.open("timcard2")
# worksheet.share("accessgoogleapis@elchaparrobackend.iam.gserviceaccount.com", perm_type='user', role='writer')
sheet = workbook.sheet1
worksheet = workbook.add_worksheet(title="Aloha", rows="100", cols="20")
for cell in sheet.range('A2:A5'):
    print(cell.value)

print(sheet.row_values(2))

sheet.update_acell('A2', 'Porn')



