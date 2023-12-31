import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
f = open('demofile.txt','r')



file_name="credentials\contest-ranking-generation-dec00c27810c.json"

creds=ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client=gspread.authorize(creds)

# sheet=client.open_by_url('https://docs.google.com/spreadsheets/d/1FlUjm0vxrkoRf1W6zvc47SzXHmqYIT3uUvH6yCNUJNE/edit#gid=0').sheet1
spread=client.open_by_url(str(f.readline()))

allsheets=spread.worksheets()

temp=[]
for sheet in allsheets:

    sheet.update_cell(1,2,"GLOBAL RATINGS")
    sheet.update_cell(1,3,"EASY")
    sheet.update_cell(1,4,"MEDIUM")
    sheet.update_cell(1,5,"HARD")
    sheet.update_cell(1,6,"TOTAL SOLVED")
    sheet.update_cell(1,7,"CONTEST ATTENDED")
    sheet.update_cell(1,8,"CONTEST RATINGS")


    python_sheet=sheet.get_all_records()

    p=list(python_sheet[0].keys())[0]

    l=[]

    for i in python_sheet:
        l.append(i[p])

    temp.append(l)


def put_data(var,i,global_rating,easy,medium,hard,total,contest_attended,contest_ranking):
    var.update_cell(i,2,global_rating)
    var.update_cell(i,3,easy)
    var.update_cell(i,4,medium)
    var.update_cell(i,5,hard)
    var.update_cell(i,6,total)
    var.update_cell(i,7,contest_attended)
    var.update_cell(i,8,contest_ranking)

def get_list(val):
    return temp[val]        