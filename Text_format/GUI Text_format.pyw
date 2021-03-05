import tkinter as tk
import tkinter.font
import pyperclip


def label(text):
    result = tk.Label(win, text=text, font=('Comic Sans MS', 13))
    result.place(x=5, y=70, height=100, width=350)


def clear_esc(event):
    entry.delete(0, 'end')
    splitter_entry.delete(0, 'end')
    label('')
    entry.focus_set()
    

def decorator(func):
    def wrapper():
        global count, text, text_list, text_new
        text_new = []
        text = entry.get()
        text = text.lower()
        text_list = sorted(list(set(text.split())))
        func()
        symbol = splitter_entry.get()
        text = symbol.join(text_new)
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

@decorator
def convert_id():
     for i in text_list:
        if 'т' not in i:
            i = 'т' + i
            text_new.append(i)
        elif 'т' in i:
            text_new.append(i)

@decorator
def convert_txt():
    for i in text_list:
        text_new.append(i)


win = tk.Tk()
win.title('Преобразование: Текста, Оферт, ID ...')
win.geometry('560x207+890+320')
win.resizable(0, 0)
win.wm_iconbitmap('txt.ico')

enter_text = tk.Label(win, text='Вставьте текст:', font=tkinter.font.Font(size=11, weight='bold'), anchor='w')
entry = tk.Entry(win, bg='white')
splitter_label = tk.Label(win, text='Вставьте разделитель:', font=tkinter.font.Font(size=11, weight='bold'), anchor='w')
splitter_entry = tk.Entry(win, bg='white', justify='center')
offer_txt = tk.Button(win, text='Оферты', font=(8), command=convert_offer)
id_txt = tk.Button(win, text='Позиции каталога (ID)', font=(8), command=convert_id)
txt = tk.Button(win, text='Любой текст', font=(8), command=convert_txt)
convert_label = tk.Label(win, text='Преобразовать:', font=tkinter.font.Font(size=11, weight='bold'), anchor='w')
win.bind('<KeyPress-Escape>', clear_esc)

enter_text.place(x=10, y=5, height=27, width=140)
entry.place(x=145, y=5, height=27, width=410)
splitter_label.place(x=10, y=37, height=27, width=190)
splitter_entry.place(x=210, y=37, height=27, width=80)
offer_txt.place(x=355, y=72, height=40, width=200)
id_txt.place(x=355, y=117, height=40, width=200)
convert_label.place(x=355, y=41, height=27, width=200)
txt.place(x=355, y=162, height=40, width=200)


entry.focus_set()
win.mainloop()
