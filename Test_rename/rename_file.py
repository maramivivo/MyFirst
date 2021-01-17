import os, traceback

bad_list = ['[Отборные Сливы] ', '[MEGASLIV.BIZ] ', '[sharewood.band] ',
            '[sharewood.biz] ', '[share-wood.biz] ', '[slivoman.com] ',
            '[BOOMINFO.RU] ', '[Infosklad.org] ', '[sliwbl.biz] ',
            '[Boominfo.ORG] ', '[www.slifki.info] ', '[SW.BAND] ',
            '[SuperSliv.BiZ] ', '[BOOMINFO.ORG] ', '[Example] ']

def rename():
    def foo(files_folders):
        for name in files_folders:
            for el in bad_list:
                if el in name:
                    new_name = name.replace(el, '')
                    try:
                        os.rename(name, new_name)
                    except FileExistsError:
                        print(traceback.print_exc(limit=0))
                                                
    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
        os.chdir(directory)
        foo(folders)
        foo(files)
    print('>>> Все папки и файлы переименованы <<<')
    
print('\nИз названий папок и файлов будут удалены следующие сочатния символов:')
for i in bad_list:
    print(i)
input('\nНажмите "Enter" для запуска файла\n')

rename()
input('\nНажмите "Enter" для выхода')

