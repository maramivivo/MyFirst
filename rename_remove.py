import os, traceback

bad_list = ['[BOOMINFO.ORG] ', '[BOOMINFO.RU] ', '[Boominfo.ORG] ',
            '[Example] ', '[Infosklad.org] ', '[MEGASLIV.BIZ] ',
            '[SW.BAND] ', '[SuperSliv.BiZ] ', '[share-wood.biz] ',
            '[sharewood.band] ', '[sharewood.biz] ', '[slivoman.com] ',
            '[sliwbl.biz] ', '[www.slifki.info] ', '[Отборные Сливы] ',
            '[Sharewood.biz] ', '[Sharewood.band] ', '[openssource.biz] ',
            '[sliwbl.com]', '[SuperSliv.Biz] ', '[SuperSliv.biz] ', '[Sliv_Qa] ']

# список названий файлов для удаления
remove_list = ['MEGASLIV.BIZ - Качай курсы беслпатно!.url',
               'Как зайти на сайт с курсами, тренингами, книгами! - boominfo.org.url',
               'SHAREWOOD_ZERKALO_COM_90000_курсов_на_нашем_форуме!.url',
               'SHAREWOOD_BAND_Платное_теперь_бесплатно!.url',
               'SHAREWOOD_BIZ_Качай_популярные_курсы.url',
               'Open-Hide.biz.url',
               'SHAREWOOD_BIZ_Платное_теперь_бесплатно!.url',
               'Infosklad.org - Скачивай платные курсы, тренинги и другие материалы - бесплатно!.url',
               '[www.slifki.info]Спасибо за загрузку!.docx',
               '[MEGASLIV.BIZ] Обязательно к прочтению.docx',
               '[SW.BAND] Прочти перед изучением!.docx',
               '[SW.BAND] Прочти перед изучением! .docx',
               '[slivoman.com] До изучения.docx',
               'Курсы, Тренинги, Книги, Семинары, Какчаем ТУТ - SuperSliv.biz.url']
CHEK_LIST = ['[sharewood.biz] Информация.docx', '[infobiza.net] Информация.docx']

def remove_files():
    def foo_remove(files):
        for name in files:
            for el in remove_list:
                if el == name:
                    os.remove(name)
##                    try:
##                        os.remove(name)
##                    except:
##                        print(traceback.print_exc(limit=0))

    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo_remove(files)
    print('\n>>> Лишние файлы удалены')
    

def rename():
    def foo_rename(files_folders):
        for name in files_folders:
            for el in bad_list:
                if el in name and name not in CHEK_LIST:
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
        foo_rename(files)
        foo_rename(folders)
    print('\n>>> Все папки и файлы переименованы\n')


def chek():
    print_chek = []
    def foo_chek(files_folders):
        for el in CHEK_LIST:
            for i in files_folders:
                if el == i:
                    if i not in print_chek:
                        print_chek.append(i)
##            print(files_folders)
    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo_chek(files)
    if print_chek:
        print('>>> Необходимо проверить следующие файлы (удалить?):')
        for i in print_chek:
            print('|',i)

print('\nИз названий папок и файлов будут удалены следующие сочатния символов:')
for i in bad_list:
    print('->', i)

print('\nБудут удалены следующие файлы:')
for i in remove_list:
    print('->', i)
input('\nНажмите "Enter" для запуска файла\n')

remove_files()
rename()
chek()

input('\nНажмите "Enter" для выхода')

##if __name__ == "__main__":
##    main()
