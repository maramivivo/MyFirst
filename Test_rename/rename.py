import os

# получение списка поддиректорий из текущей директории
def get_subdirectories ():
    current_directory = os.getcwd()
    list_directory = []
    for i in os.walk(current_directory):
        list_directory.append(i[0])
    return list_directory

# переименование файлов и папок в текущей директории
def renaming(directory, bad_symbols):
##    bad_symbols = input('Введите текст, который нужно удалить\n')
    new_name_list = []
    for i in list(os.listdir(directory)): # перебор имён файлов в текущей директории
        if bad_symbols in i:
            name_replace = i.replace(bad_symbols, '')
            os.replace(i, name_replace)
    print('Переименование файлов (папок) завершено')

##for element in get_subdirectories():
##    renaming(element)

a = get_subdirectories()
bad_symb = input('Введите текст, который нужно удалить\n')
for i in a:
    renaming(i, bad_symb)

