def div_num(n):
    a = 0
    try:
        if n_1 % n == 0:
            a = int(n_1 / n)
        elif n_1 % n != 0:
            a = round(n_1 / n, 5)
        return a
    except ZeroDivisionError:
        print('Возникла ошибка: Деление на ноль невозможно. ', end='')
##print(div_num(2))
##print(div_num(12))
##print(div_num(0))
##print(div_num(1))

n_1 = float(input('Введите "Делимое"\n'))
n = float(input('Введите "Делитель"\n'))

print(div_num(n))

input()
