import tkinter as tk
import pyperclip


def label(text):
    result = tk.Label(win, text=text, font=('Comic Sans MS', 12))
    result.place(x=5, y=50, height=100, width=340)


def clear_esc(event):
    entry.delete(0, 'end')
    label('')
    

def decorator(func):
    def wrapper():
        global text, text_list, text_new
        text_new = []
        text = entry.get()
        text = text.lower()
        text_list = sorted(list(set(text.split())))
        func()
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
        pyperclip.copy(text)
        if count-1 == 0:
            label(f'Введите текст')
        else:
            label(f'Текст преобразован и скопирован.\nКоличество элементов: {count-1}')
    return wrapper




@decorator    
def convert_offer():
    for i in text_list:
        if 'оф-2021-' in i:
            text_new.append(i)
        elif 'оф-2020-' in i:
            text_new.append(i)
        elif 'оф-2021-' not in i:
            i = 'оф-2021-' + i
            text_new.append(i)
       label(f'Текст преобразован и скопирован.\nКоличество элементов: {count-1}')
    

@decorator 
def convert_id():
    ...


@decorator 
def convert_txt():
    ...





win = tk.Tk()
win.title('Преобразование номеров оферт и ID')
win.geometry('550x180+890+320')

enter = tk.Label(win, text='Поле для ввода текста', font=(12))
entry = tk.Entry(win, bg='white')
offer_txt = tk.Button(win, text='Преобразовать\nоферты', command=convert_offer)
id_txt = tk.Button(win, text='Преобразовать\nID', command=convert_id)
txt = tk.Button(win, text='Преобразовать другой\nтекст и скопировать его', command=convert_txt)#, command=copy_txt)

win.bind('<KeyPress-Escape>', clear_esc)

enter.place(x=5, y=5, height=40, width=200)
entry.place(x=210, y=5, height=27, width=335)
offer_txt.place(x=345, y=50, height=40, width=200)
id_txt.place(x=345, y=95, height=40, width=200)
txt.place(x=345, y=135, height=40, width=200)


entry.focus_set()
win.mainloop()
