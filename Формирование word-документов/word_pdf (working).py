import openpyxl
from docxtpl import DocxTemplate
import os
import comtypes.client
import time

##input('Нажмите "Enter" для запуска скрипта\n')

wb = openpyxl.load_workbook('Данные\\Данные.xlsx')
sheet = wb.active
n = sheet.max_row
save_location = input('Введите адрес сохранения\n')
if not os.path.isdir(save_location):
    os.makedirs(save_location)
save_location_pdf = save_location + '\\PDF'
if not os.path.isdir(save_location_pdf):
    os.mkdir(save_location_pdf)

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
        file = company[company.index('"')+1:-1]
        save_location_word = save_location + f'\\Письмо [{file}].docx'
        doc.save(save_location_word)

        #новый фрагмент (создание pdf-файлов)

        wdFormatPDF = 17
        
        in_file = save_location_word
        out_file = save_location_pdf + f'\\Письмо [{file}].pdf'
        
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = True
        time.sleep(3)

        doc=word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Visible = False
        break

word.Quit()
print ('Формирование документов завершено')
