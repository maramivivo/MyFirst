# Игра в кости
import random

game = input('Нажми "Пробел" и "Enter", чтобы бросить кубик\n')
while game == ' ':
#if game == ' ':
    cub = random.randint(1, 7)
    print(cub)
    game = input('Если хочешь продолжить игру, нажми "Пробел" и "Enter".\nЕсли хочешь окончить игру, нажми любую другую клавишу.\n')
else:
    print('Игра окончена\n')

input('Нажми \'Enter\' для выхода\n')
