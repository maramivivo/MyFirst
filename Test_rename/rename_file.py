import os

dirr = os.getcwd()

bad_list = ['[Отборные Сливы] ', '[MEGASLIV.BIZ] ', '[sharewood.band] ',
            '[sharewood.biz] ', '[share-wood.biz] ', '[slivoman.com] ',
            '[BOOMINFO.RU] ', '[Infosklad.org] ', '[sliwbl.biz] ',
            '[Boominfo.ORG] ', '[www.slifki.info] ', '[SW.BAND] ',
            '[SuperSliv.BiZ] ', '[BOOMINFO.ORG] ']

bs = input('Ввести все символы, подлежащие удалению (включая пробелы)\n')

files = os.listdir(dirr)
for f in files:
    if bs in f:
        new_f = f.replace(bs, '')
        os.rename(f, new_f)

print(bad_list)
input()
