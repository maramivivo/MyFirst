import os

#получение списка поддиректорий из текущей директории
def get_subdirectories ():
    current_directory = os.getcwd()
    list_directory = []
    for i in os.walk(current_directory):
        list_directory.append(i[0])
    return list_directory

#переименование файлов и папок в текущей директории
#!!! дописать функцию согласно примера ниже
def renaming(directory):
    bad_symbols = input('Введите текст, который нужно удалить\n')
    new_name_list = []
    for i in list(os.listdir(directory)):
        if bad_symbols in i:
            os.rename(i, i - bad_symbols)



#Пример для функции "renaming"
d = ['[Example] Text_1', '[Example] Text_2']
new = []
for i in d:
    if '[Example] ' in i:
        a = i.replace('[Example] ', '')
        new.append(a)
print(new)

