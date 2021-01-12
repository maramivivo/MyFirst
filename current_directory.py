import os

# вывести текущую директорию
a = os.getcwd()
b = os.listdir(a)
print("Текущая деректория: (", a, ")\n")
print("Список объектов:")
#for i in b:
#    print(i)

num = 1
for i in b:
    print(num, '. ', i, sep = '')
    num += 1
    
input()
