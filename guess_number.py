print('Игра: "Угадай число"\n')

n_min = 25
n_max = 46
n_real = 38
print('Я загадал целое число в интервале от', n_min, 'до', n_max, '. Попробуйте его угадать.' )
n_user = ''
# choic = ''


while n_user != n_real:
    for i in range(1, 999**999):
        n_user = int(input('Ваш вариант:\n'))
        if n_user < n_real:
            print('Предложенное число меньше задуманного\n')
            i += 1
        elif n_user > n_real:
            print('Предложенное число больше задуманного\n')
            i += 1
        elif n_user == n_real:
            print('Верно! Количество попыток: ', i)
            break

input()

