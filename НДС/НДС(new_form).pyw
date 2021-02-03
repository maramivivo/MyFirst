import tkinter as tk

def copy_result():
    pass

def clear():
    pass


win = tk.Tk()
win.geometry('550x215+960+420')
win.resizable(0, 0)

entry = tk.Entry(win, bg='white', bd=2,
                 font=('Comic Sans MS', 20), justify='right', fg='grey45')
enter = tk.Label(win, text='Введите сумму с налогом:',
                 font=('Comic Sans MS', 12), fg='grey43')

nds_10 = tk.Label(win, text='НДС 10%', font=('Comic Sans MS', 10),
                  fg='grey43')
nds_20 = tk.Label(win, text='НДС 20%', font=('Comic Sans MS', 10),
                  fg='grey43')
btn_calculate = tk.Button(win, text='Рассчитать\n(Enter)', font=('Tahoma', 18),
                          fg='grey45',command=copy_result)
btn_clear = tk.Button(win, text = 'Очистить\n(Esc)',
                      font=('Tahoma', 18), fg='grey45', command=clear)

entry.place(x=230, y=5, height=40, width=315)
enter.place(x=5, y=5, height=40, width=220)
nds_10.place(x=5, y=50, height=40, width=150)
nds_20.place(x=160, y=50, height=40, width=150)
btn_calculate.place(x=360, y=60, height=70, width=185)
btn_clear.place(x=360, y=135, height=70, width=185)


win.mainloop()
