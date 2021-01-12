"""
Последовательность Коллатца

Берём любое натуральное число n. Если оно чётное, то делим его на 2, а если нечётное,
то умножаем на 3 и прибавляем 1 (получаем 3n + 1). Над полученным числом выполняем
те же самые действия, и так далее.

Гипотеза Коллатца заключается в том, что какое бы начальное число n мы ни взяли,
рано или поздно мы получим единицу.
"""
def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


def collatz_iterations(num):
    list_num = []
    while num != 1:
        num = collatz(num)
        list_num.append(num)
    print('Число итераций: ', len(list_num))
    print('Последовательность Коллатца:', list_num)
    print('Минимальное значение промежуточных результатов: ', min(list_num))
    print('Максимальное: ', max(list_num))
    print('Среднее значение: ', round(sum(list_num)/len(list_num), 2))
    return list_num


n = int(input('Введите целое число\n'))
print()
collatz_iterations(n)
input()
