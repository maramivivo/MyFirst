import os

#получение списка поддиректорий из текущей директории
def get_subdirectories ():
    current_directory = os.getcwd()
    list_directory = []
    for i in os.walk(current_directory):
        list_directory.append(i[0])
    return list_directory

#переименование файлов и папок в текущей директории
def renaming(directory):
    bad_symbols = input('Введите текст, который нужно удалить\n')
    name_files = []
    for i in list(os.listdir(directory)):
        if bad_symbols in i:
            os.rename(i, i - bad_symbols)




d = os.getcwd()
    
print(d)
