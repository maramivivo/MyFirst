import os
'''
По факту происходит переименование нескольких верхних уровней, в глубь скрипт не идёт (Почему!?)
'''

bad_list = ['[Отборные Сливы] ', '[MEGASLIV.BIZ] ', '[sharewood.band] ',
            '[sharewood.biz] ', '[share-wood.biz] ', '[slivoman.com] ',
            '[BOOMINFO.RU] ', '[Infosklad.org] ', '[sliwbl.biz] ',
            '[Boominfo.ORG] ', '[www.slifki.info] ', '[SW.BAND] ',
            '[SuperSliv.BiZ] ', '[BOOMINFO.ORG] ', '[Example] ']
startdir = os.getcwd()

def my_rename():
    for directory, folder, file in os.walk(os.getcwd()): # начало цикла из текущей директории (где находится файл)
        os.chdir(directory)
        for f in file:
            if file:
                for i in bad_list:
                    if i in f:
                        new_f = f.replace(i, '')
                        os.rename(f, new_f)
        print('Переименование файлов завершено\n\n')

        for fold in folder:
            if folder:
                for i in bad_list:
                    if i in fold:
                        new_fold = fold.replace(i, '')
                        try:
                            os.rename(fold, new_fold)
                        except:
                            continue
        print('Переименование папок завершено\n')
        
    os.chdir(startdir)
            

my_rename()
print('\n=========================================\n\nПереименование всех данных завершено')
print(os.getcwd())
input()
