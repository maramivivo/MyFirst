import tkinter as tk

win = tk.Tk()
win.title('Калькулятор Налогов')
win.geometry('500x190+990+420')
win.resizable(False, False)

enter = tk.Label(win, text='Введите сумму с налогом:', font=('Comic Sans MS', 10), fg='grey')
enter.place(x=5, y=5, height=40, width=190)

entry = tk.Entry(win, bg='white', bd=2, font=('Comic Sans MS', 20), justify='right', fg='grey')
entry.place(x=195, y=5, height=40, width=300)

#====

btn_nds_20 = tk.Button(win, text='Посчитать НДС (20%)', font=('Tahoma', 15), fg='grey')
btn_nds_20.place(x=260, y=50, height=40, width=235)

btn_nds_10 = tk.Button(win, text='Посчитать НДС (10%)', font=('Tahoma', 15), fg='grey')
btn_nds_10.place(x=260, y=95, height=40, width=235)

result_win = tk.Label(win, text='123 456.78', font=('Comic Sans MS', 30), fg='grey', relief='ridge')
result_win.place(x=5, y=50, height=85, width=250)

btn_copy = tk.Button(win, text='Скопировать', font=('Tahoma', 15), fg='grey')
btn_copy.place(x=5, y=140, height=45, width=490)


entry.focus_set()
win.mainloop()
