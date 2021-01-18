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
               'Обязательно к прочтению.docx',
               '[SW.BAND] Прочти перед изучением!.docx',
               'Прочти перед изучением!.docx'
               '[slivoman.com] До изучения.docx',
               'До изучения.docx'] 

def remove_files():
    def foo_remove(files):
        for name in files:
            for el in remove_list:
                if el == name:
                    try:
                        os.remove(name)
                    except:
                        print(traceback.print_exc(limit=0))

    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo_remove(files)
    print('>>> Лишние файлы удалены\n')


def rename():
    def foo_rename(files_folders):
        for name in files_folders:
            for el in bad_list:
                if el in name:
                    new_name = name.replace(el, '')
                    try:
                        os.rename(name, new_name)
                    except FileExistsError:
                        print('!!!')
                        print(traceback.print_exc(limit=0))
                    except PermissionError:
                        print(traceback.print_exc(limit=0))

    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo_rename(folders)
        foo_rename(files)
    print('\n>>> Все папки и файлы переименованы')
    
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
