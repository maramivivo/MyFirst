import pyperclip as pp
import tkinter as tk

##file = open(r'Текст.txt', '+', encoding='utf8')
##text = file.read()

'''
text = ''
text = text.lower()
choice = int(input('Введите:\nДля преобразования "ОФЕРТ" -------- >>> 1 <<<\nДля преобразования "ID" ----------- >>> 2 <<<\nДля преобразования другого текста - >>> 3 <<<\n'))


print('')
text_list = set(text.split())
text_list = sorted(list(text_list))
text_new = []


for i in text_list:
    if choice == 1:
        if 'оф-2020-' not in i:
            i = 'оф-2020-' + i
            text_new.append(i)
        elif 'оф-2020-' in i:
            text_new.append(i)
    elif choice == 2:
        if 'т' not in i:
            i = 'т' + i
            text_new.append(i)
        elif 'т' in i:
            text_new.append(i)
    elif choice == 3: #просто соеденялка
        text_new.append(i)
        
       
text = '|'.join(text_new)
count = 1
for i in text_new:
    if len(str(count)) == 1:
        print(count, '   ', i, sep = '')
    elif len(str(count)) == 2:
        print(count, '  ', i, sep = '')
    else:
        print(count, ' ', i, sep = '')
    count +=1
'''





win = tk.Tk()
win.title('Преобразование номеров оферт и ID')
win.geometry('550x180+890+320')

enter = tk.Label(win, text='Поле для ввода текста', font=(12))
entry = tk.Text(win, bg='white')
offer_txt = tk.Button(win, text='Преобразовать\nоферты')
id_txt = tk.Button(win, text='Преобразовать\nID')
txt = tk.Button(win, text='Преобразовать другой\nтекст и скопировать его')#, command=copy_txt)

enter.place(x=5, y=5, height=40, width=200)
entry.place(x=210, y=5, height=40, width=335)
offer_txt.place(x=345, y=50, height=40, width=200)
id_txt.place(x=345, y=95, height=40, width=200)
txt.place(x=345, y=135, height=40, width=200)

def copy_txt():
    text = entry.get()
    print(type(text), text)
    file = open(r'Текст.txt', '+', encoding='utf8')
    rec_text = file.read()

##pp.copy(text) #копирование текста в буфер обмена

##file.close()

entry.focus_set()
win.mainloop()
