import datetime
import openpyxl as xl
wb = xl.load_workbook('Контакты.xlsx')
sheet = wb.active
today = datetime.date.today()
for i in range(1, sheet.max_row):
    people = sheet['A' + str(i + 1)].value
    birthday = sheet['B' + str(i + 1)].value
##    print(birthday.day)
if birthday.day == today.day and birthday.month == today.month:
    print(f'Сегодня {people} отмечает своё день рождения')
'''
    if len(str(i)) == 1:
        n = str(i) + '.  '
    elif len(str(i)) == 2:
        n = str(i) + '. '
    elif len(str(i)) == 3:
        n = str(i) + '.'
    print(n, people, ' - ', birthday, sep='')
'''
