import os
import tkinter as tk

def update_PIP():
    os.system('start cmd /k python.exe -m pip install --upgrade pip') 
 
win = tk.Tk()
win.title('Обновление PIP')
win.geometry('300x120+1100+500')
win.resizable(0, 0)
win.attributes('-topmost', True)
win.wm_iconbitmap('pip.ico')

btn_pip_update = tk.Button(win, text='Обновить PIP', font=('CharterC', 30, 'bold'), fg='blue2', bg='green2', command=update_PIP)
btn_pip_update.place(x=1, y=1, height=118, width=298)


##canvas1 = tk.Canvas(root, width = 300, height = 350,
##                    bg = 'lightsteelblue2', relief = 'raised')
##canvas1.pack()
## 
####label1 = tk.Label(root, text='Обновление PIP', bg = 'lightsteelblue2')
##label1.config(font=('helvetica', 20))
##canvas1.create_window(100, 80, window=label1)
## 
##def upgradePIP ():
##    os.system('start cmd /k python.exe -m pip install --upgrade pip') 
##    
##button1 = tk.Button(text='      Обновить PIP     ', command=upgradePIP,
##                    bg='green', fg='white', font=('helvetica', 12, 'bold'))
##canvas1.create_window(150, 180, window=button1)
 
win.mainloop()
