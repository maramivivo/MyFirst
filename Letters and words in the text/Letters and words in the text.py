#подсчёт количества встречающихся в тексте букв
#текст берётся из файла text.txt, который должен быть и располагаться в одной директории с настоящим скриптом

import pyperclip #модуль для копирования в буфер обмена
import webbrowser #модуль для перехода по ссылке в браузере


#функция получения списка букв в тексте в алфавитном порядке
def countt(text):
  text = text.lower()
  count_list = []
  abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
  for i in text:
    if i in abc:
      count_list.append(i)
  return sorted(count_list)

  
#получение уникальных значений текста (из полученного списка)
def unic(func, text):
  count_unic = []
  count_list = func(text)
  for i in count_list:
    if i not in count_unic:
      count_unic.append(i)
  return count_unic
   

#количество каждой буквы в тексте
def char(unic, countt, text):
  count_list = countt(text)      #1 функция
  char_unic = unic(countt, text) #2 функция
  char_list = []
  for i in char_unic:
    char_count = count_list.count(i) #целое число (количество вхождений)
    element = (i, char_count)
    char_list.append(element)
  char_sort = sorted(char_list, key=lambda char: char[1], reverse=True) #сортировка букв по их количеству
  return char_sort #char_list


#возвращает количество слов в тексте
def words(text):
    bad_chars = ['.,?!;:/|+<>\\[]\()1234567890№"\'', ' -', '- ']
    for i in bad_chars[0]:
        text = text.replace(i, ' ')
    if bad_chars[1] or bad_chars[2] in text:
        text = text.replace(bad_chars[1], ' ')
        text = text.replace(bad_chars[2], ' ')
    text = text.split()
    count = 0
    for i in text:
        count += 1
    return count


#выбор и открытие и чтение текстового файла

#в данном случае необходимо создать файл с КОНКРЕТНЫМ именем 'text.ru'
file_name = 'text.txt'
file = open(file_name, 'r', encoding='utf-8')
text = file.read()

text_for_copy_list = []
func = char(unic, countt, text)
words_count = 'Слов в тексте: ' + str(words(text)) + '\n\nБукв в тексте:'
print(words_count)
for i in func[:11]:                 #вывод первых 10 позиций из списка (буквы с их количеством)
  a = i[0].upper() + ' - ' + str(i[1])
  text_for_copy_list.append(a)
  print(i[0].upper(), '-', i[1])
text_for_copy = '=====================\n' + words_count + '\n' + '\n'.join(text_for_copy_list)
pyperclip.copy(text_for_copy) #копирование текста в буфер обмена
print('\nПредставленная информация скопирована в буфер обмена...\n')

file.close


url = 'https://trepsy.net/razvit/stat.php?stat=1654#yandex_rtb_R-A-252052-3:~:text=13.10.2009-,%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5' #инструкция
try:
  manual = int(input('Введи "0" для открытия инструкции для Упражнения "Ищем буквы"\nили любую другую кнопку для выхода\n'))
  if manual == 0:
    webbrowser.open(url, new=2)
    input('Нажми Enter для выхода')
  else:
    input('Нажми Enter для выхода')
except ValueError:
  input('Нажми Enter для выхода')
