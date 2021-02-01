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
        summ = summ.replace('.', ',')
    summ = float(summ)
    return summ


def asd(x):
    global result
    result = convert_nalog(copy_input(), x)
    result_win = tk.Label(win, text=result, font=('Comic Sans MS', 30), fg='grey', relief='ridge')
    result_win.place(x=5, y=50, height=85, width=250)


def foo_nds_10():    
    asd(10)


def foo_nds_20():
    asd(20)    


def copy_result():
    pyperclip.copy(result)


win = tk.Tk()
win.title('Калькулятор Налогов')
win.geometry('500x190+890+320')
win.resizable(False, False)

enter = tk.Label(win, text='Введите сумму с налогом:', font=('Comic Sans MS', 10), fg='grey')
entry = tk.Entry(win, bg='white', bd=2, font=('Comic Sans MS', 20), justify='right', fg='grey')
btn_nds_20 = tk.Button(win, text='Посчитать НДС (20%)', font=('Tahoma', 15), fg='grey', command=foo_nds_20)
btn_nds_10 = tk.Button(win, text='Посчитать НДС (10%)', font=('Tahoma', 15), fg='grey', command=foo_nds_10)
btn_copy = tk.Button(win, text='Скопировать', font=('Tahoma', 15), fg='grey', command=copy_result)

btn_nds_20.place(x=260, y=50, height=40, width=235)
btn_nds_10.place(x=260, y=95, height=40, width=235)
btn_copy.place(x=5, y=140, height=45, width=490)
entry.place(x=195, y=5, height=40, width=300)
enter.place(x=5, y=5, height=40, width=190)

entry.focus_set()
win.mainloop()
