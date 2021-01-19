import os, traceback

bad_list = ['[BOOMINFO.ORG] ', '[BOOMINFO.RU] ', '[Boominfo.ORG] ',
            '[Example] ', '[Infosklad.org] ', '[MEGASLIV.BIZ] ',
            '[SW.BAND] ', '[SuperSliv.BiZ] ', '[share-wood.biz] ',
            '[sharewood.band] ', '[sharewood.biz] ', '[slivoman.com] ',
            '[sliwbl.biz] ', '[www.slifki.info] ', '[Отборные Сливы] ']

# список названий файлов для удаления
remove_list = ['MEGASLIV.BIZ - Качай курсы беслпатно!.url',
               'SHAREWOOD_ZERKALO_COM_90000_курсов_на_нашем_форуме!.url',
               '[www.slifki.info]Спасибо за загрузку!.docx',
               '[MEGASLIV.BIZ] Обязательно к прочтению.docx',
               '[SW.BAND] Прочти перед изучением!.docx',
               '[slivoman.com] До изучения.docx',
               '[infobiza.net] Информация.docx'] 

# одинковая часть
'''def rename():
    def foo(f, my_list):
        for name in f:
            for el in my_list:
...

'''

def my_remove():
    def foo(f, my_list):
        for name in f:
            for el in my_list:
                # различающаяся часть
                if el == name:
                    try:
                        os.remove(name)
                    except:
                        print(traceback.print_exc(limit=0))
                # ***

    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo(files, remove_list) # отличающаяся часть
    print('>>> Лишние файлы удалены\n') # отличающаяся часть


def rename():
    def foo(f, my_list):
        for name in f:
            for el in my_list:
                # различающаяся часть
                if el in name:
                    new_name = name.replace(el, '')
                    try:
                        os.rename(name, new_name)
                    except FileExistsError:
                        print('!!!')
                        print(traceback.print_exc(limit=0))
                    except PermissionError:
                        print(traceback.print_exc(limit=0))
                # ***

    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo(folders, bad_list) # отличающаяся часть
        foo(files, bad_list) # отличающаяся часть
    print('\n>>> Все папки и файлы переименованы') # отличающаяся часть
    


print('\nИз названий папок и файлов будут удалены следующие сочатния символов:')
for i in bad_list:
    print('->', i)

print('\nБудут удалены следующие файлы:')
for i in remove_list:
    print('->', i)
input('\nНажмите "Enter" для запуска файла\n')

remove_files()
rename()
input('\nНажмите "Enter" для выхода')

if __name__ == "__main__":
    main()
