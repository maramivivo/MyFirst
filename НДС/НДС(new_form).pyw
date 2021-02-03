import tkinter as tk
import pyperclip

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


def clear():
    entry.delete(0, 'end')
    result_win_10 = tk.Button(win, text='', font=('Comic Sans MS', 20), fg='navy')
    result_win_10.place(x=5, y=85, height=85, width=150)
    result_win_20 = tk.Button(win, text='', font=('Comic Sans MS', 20), fg='navy')
    result_win_20.place(x=160, y=85, height=85, width=150)

def clear_esc(event):
    clear()


def clear_clipboard(event):
    if str(event.type) == 'Esc':
        clear()


def asd(x):
    def copy_result():
        if result != 'Введите сумму':
            pyperclip.copy(result)
    try:
        result = convert_nalog(copy_input(), x)
    except ValueError:
        result = 'Введите\nсумму'
    if result == 'Введите\nсумму':
        result_vew = result
    else:
        result_vew = result + ' ₽'
    copy_result()
    result_win_10 = tk.Button(win, text=result_vew, font=('Comic Sans MS', 20), fg='navy', command=copy_result)
    result_win_10.place(x=5, y=85, height=85, width=150)
    result_win_20 = tk.Button(win, text=result_vew, font=('Comic Sans MS', 20), fg='navy', command=copy_result)
    result_win_20.place(x=160, y=85, height=85, width=150)


def foo_nds():
    def foo():
        asd(10)
        asd(20)
    a = foo()
    return a

        
def foo_nds_enter(event):
    if str(event.type) == 'Return':
        foo_nds()
    

win = tk.Tk()
win.title('Калькулятор Налогов')
win.geometry('550x215+960+420')
win.resizable(0, 0)
win.wm_iconbitmap('icon.ico')

entry = tk.Entry(win, bg='white', bd=2,
                 font=('Comic Sans MS', 20), justify='right', fg='grey45')
enter = tk.Label(win, text='Введите сумму с налогом:',
                 font=('Comic Sans MS', 12), fg='grey43')

nds_10 = tk.Label(win, text='НДС 10%', font=('Comic Sans MS', 10),
                  fg='grey43')
nds_20 = tk.Label(win, text='НДС 20%', font=('Comic Sans MS', 10),
                  fg='grey43')
btn_calculate = tk.Button(win, text='Рассчитать\n(Enter)', font=('Tahoma', 18),
                          fg='grey45',command=foo_nds)
btn_clear = tk.Button(win, text = 'Очистить\n(Esc)',
                      font=('Tahoma', 18), fg='grey45', command=clear)
win.bind('<KeyPress-Escape>', clear_esc)
win.bind('<KeyRelease-Return>', foo_nds_enter)

entry.place(x=230, y=5, height=40, width=315)
enter.place(x=5, y=5, height=40, width=220)
nds_10.place(x=5, y=50, height=40, width=150)
nds_20.place(x=160, y=50, height=40, width=150)
btn_calculate.place(x=360, y=60, height=70, width=185)
btn_clear.place(x=360, y=135, height=70, width=185)


entry.focus_set()
win.mainloop()
