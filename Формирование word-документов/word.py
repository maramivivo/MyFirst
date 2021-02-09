import openpyxl
from docxtpl import DocxTemplate


##input('Нажмите "Enter" для запуска скрипта\n')

wb = openpyxl.load_workbook('Данные\\Данные.xlsx')
sheet = wb.active
n = sheet.max_row
save_location = input('Введите адрес сохранения\n')

if '\\' in save_location:
    save_location.replace('\\', '\\\\')                 

for i in range(n):
    if i < (n-1):
        company = sheet['A' + str(i + 2)].value
        adress = sheet['B' + str(i + 2)].value
        post = sheet['C' + str(i + 2)].value
        short_director = sheet['D' + str(i + 2)].value
        initials = sheet['E' + str(i +2 )].value
        doc = DocxTemplate('Данные\\Письмо_шаблон.docx')
        context = {'company': company, 'adress': adress, 'post': post,
                   'short_director': short_director, 'initials': initials}
        doc.render(context)
        file = sheet['F' + str(i + 2)].value
        save_location_word = save_location + f'\\Письмо _{file}.docx'
        doc.save(save_location_word)
        
##        print(f'Письмо _{file}.docx')
        break

input('Нажмите "Enter" для выхода')
