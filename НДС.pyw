import tkinter as tk
import pyperclip

def convert_nalog(summ, tax):
    nds = round(summ*tax/(100+tax), 2)
    return nds

summ = 0
result = 0
white_list = '0123456789.,'


# GUI
win = tk.Tk()
win.title('Калькулятор Налогов')
win.geometry('500x190+890+320')
win.resizable(False, False)

enter = tk.Label(win, text='Введите сумму с налогом:', font=('Comic Sans MS', 10), fg='grey')
enter.place(x=5, y=5, height=40, width=190)

entry = tk.Entry(win, bg='white', bd=2, font=('Comic Sans MS', 20), justify='right', fg='grey')
entry.place(x=195, y=5, height=40, width=300)


def copy_input():
    global summ
    summ = entry.get()
    if ',' in summ:
        summ = summ.replace(',', '.')

        
    summ = float(summ)
    return summ



def foo_nds_10():
    global result
    result = convert_nalog(copy_input(), 10)
    result_win = tk.Label(win, text=result, font=('Comic Sans MS', 30), fg='grey', relief='ridge')
    result_win.place(x=5, y=50, height=85, width=250)
btn_nds_10 = tk.Button(win, text='Посчитать НДС (10%)', font=('Tahoma', 15), fg='grey', command=foo_nds_10)
btn_nds_10.place(x=260, y=95, height=40, width=235)


def foo_nds_20():
    global result
    result = convert_nalog(summ, 20)
    result_win = tk.Label(win, text=result, font=('Comic Sans MS', 30), fg='grey', relief='ridge')
    result_win.place(x=5, y=50, height=85, width=250)
btn_nds_20 = tk.Button(win, text='Посчитать НДС (20%)', font=('Tahoma', 15), fg='grey', command=foo_nds_20)
btn_nds_20.place(x=260, y=50, height=40, width=235)


def copy_result():
    pyperclip.copy(result)

    
btn_copy = tk.Button(win, text='Скопировать', font=('Tahoma', 15), fg='grey', command=copy_result)
btn_copy.place(x=5, y=140, height=45, width=490)




entry.focus_set()
win.mainloop()
