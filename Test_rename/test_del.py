def decorator_1(foo): #remove
    def decorator_2(files_folders):
        for name in files_folders:
            foo()
        
        
            
    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo_remove(files)
    print('>>> Лишние файлы удалены\n')


def rename():


def foo():
for el in remove_list:
    if el == name:
        try:
            os.remove(name)
        except:
             print(traceback.print_exc(limit=0))
