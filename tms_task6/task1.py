import json
import csv
from openpyxl import Workbook

def add_to_json_file():
    person = [
    {'Name' : 'Kosta', 
    'Age' : 25},
    {'Name' : 'Oleg',
    'Age' : 30}
    ]
    data = json.dumps(person, indent = 4)
    with open('json_file.json', 'w') as file_object:
        file_object.writelines(data)

def add_to_csv_file():
    fieldnames = ['Name', 'Age']
    rows = [
        {'Name' : 'Kosta',
        'Age' : 25},
        {'Name' : 'Oleg',
        'Age' : 39}
        ]
    with open('csv_file.csv', 'w') as file_object:
        writer = csv.DictWriter(file_object, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def add_to_xl_file():
    excel_file = Workbook()
    excel_sheet = excel_file.create_sheet(title='Users', index=0)
    users_rows = (
        ('Name', 'Age'),
        ('Kosta', 25),
        ('Oleg', 30)
    )

    for row in users_rows:
        excel_sheet.append(row)
        
    excel_file.save(filename="xl_file.xlsx")