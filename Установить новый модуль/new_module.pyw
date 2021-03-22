import os
import tkinter as tk

def install_module():
    module = entry.get() #C:\Program Files\Python39\Lib
    os.system('start cmd /k C:\\Program Files\\Python39\\Lib\\' + module)

win = tk/Tk()
win.title('Установка модулей')
wingeometry('300x120')


win.mainloop()

##module = '\\text'
##t = 'start cmd /k C:\\Program Files\\Python39\\Lib' + module
##
##print(t)
