import os

input('Нажмите "Enter" для запуска файла\n')
bad_list = ['[Отборные Сливы] ', '[MEGASLIV.BIZ] ', '[sharewood.band] ',
            '[sharewood.biz] ', '[share-wood.biz] ', '[slivoman.com] ',
            '[BOOMINFO.RU] ', '[Infosklad.org] ', '[sliwbl.biz] ',
            '[Boominfo.ORG] ', '[www.slifki.info] ', '[SW.BAND] ',
            '[SuperSliv.BiZ] ', '[BOOMINFO.ORG] ', '[Example] ']
startdir = os.getcwd()

def rename():
    reverse_walk = list(os.walk(os.getcwd()))[::-1]
    for directory, folders, files in reverse_walk:
##        print(directory, folders, files, sep = '\n', end = '\n===\n\n')
        os.chdir(directory)
        for folder in folders:
            for el in bad_list:
                if el in folder:
                    new_folder = folder.replace(el, '')
                    os.rename(folder, new_folder)
        print('Все папки переименованы\n')

        for file in files:
            for el in bad_list:
                if el in file:
                    new_file = file.replace(el, '')
                    os.rename(file, new_file)
        print('Все файлы переименованы')
rename()
