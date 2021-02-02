import tkinter as tk
import pyperclip

white_list = '0123456789.,'

def convert_nalog(summ, tax):
    nds = round(summ*tax/(100+tax), 2)
    if float(nds) == int(nds):
        nds = str(nds) + '0'
    nds = str(nds)
    nds = nds.replace('.', ',')
    return nds


def copy_input():
    summ = entry.get()
    if ',' in summ:
        summ = summ.replace(',', '.')
    summ = float(summ)
    return summ


def asd(x):
    def copy_result():
        if result != 'Введите сумму':
            pyperclip.copy(result)
    try:
        result = convert_nalog(copy_input(), x)
    except ValueError:
        result = 'Введите сумму'
    if result == 'Введите сумму':
        result_vew = result
    else:
        result_vew = result + ' ₽'
    copy_result()
    result_win = tk.Button(win, text=result_vew, font=('Comic Sans MS', 25), fg='navy', command=copy_result)
    result_win.place(x=5, y=65, height=85, width=290)


def foo_nds_10():    
    asd(10)


def foo_nds_20():
    asd(20)    


def clear():
    entry.delete(0, 'end')
    result_win = tk.Button(win, text='', font=('Comic Sans MS', 25), fg='navy')
    result_win.place(x=5, y=65, height=85, width=290)

def clear_esc(event):
    clear()

def clear_clipboard(event):
    if str(event.type) == 'Esc':
        clear()


win = tk.Tk()
win.title('Калькулятор Налогов')
win.geometry('550x215+890+320')
win.resizable(False, False)
win.wm_iconbitmap('icon.ico')
##win.attributes('-topmost', True) # расположение поверх всех окон

enter = tk.Label(win, text='Введите сумму с налогом:', font=('Comic Sans MS', 12), fg='grey43')
entry = tk.Entry(win, bg='white', bd=2, font=('Comic Sans MS', 20), justify='right', fg='grey45')
btn_nds_20 = tk.Button(win, text='Посчитать НДС (20%)', font=('Tahoma', 15), fg='grey43', command=foo_nds_20)
btn_nds_10 = tk.Button(win, text='Посчитать НДС (10%)', font=('Tahoma', 15), fg='grey43', command=foo_nds_10)
btn_clear = tk.Button(win, text = 'Очистить поле ввода (Esc)', font=('Tahoma', 14), fg='grey43', command=clear)
win.bind('<KeyPress-Escape>', clear_esc)
line = tk.Label(win,bg='grey37')

btn_nds_20.place(x=300, y=65, height=40, width=245)
btn_nds_10.place(x=300, y=110, height=40, width=245)
btn_clear.place(x=300, y=155, height=40, width=245)
entry.place(x=240, y=5, height=40, width=305)
enter.place(x=5, y=5, height=40, width=230)
line.place(x=10, y = 53, height=2, width=530)

entry.focus_set()
win.mainloop()
