import os

dirr = os.getcwd()
##print(dirr)

bs = input('Ввести символы, полдежащие удалению (включая пробелы)\n')
files = os.listdir(dirr)
for f in files:
##    print(f)
##    print('==========\n')
    if bs in f:
        new_f = f.replace(bs, '')
        os.rename(f, new_f)
##        print(new_f)
