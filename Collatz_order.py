def сollatz(n):
    if n % 2 == 0:
        return(n // 2)
    else:
        return(3 * n + 1)


number = int(input('Введите целое число\n'))
print()
list_number = []
while number != 1:
    сollatz(number)
    number = сollatz(number)
    #print(number)
    list_number.append(number)
print(list_number)
print('Число итераций: ', len(list_number))
print('Минимальное значение в ходе расчёта:', min(list_number))
print('Максимальное значение в ходе расчёта:', max(list_number))

input()
