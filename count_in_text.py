#file = input('Введите название (без расширения) текстового файла (*.txt)\n')
#file = file + '.txt'
#text_open = open(file, encoding='utf8')
#text = text_open.read()
text = input('Вставьте текст для подсчёта количества слов\n').lower()

#text_low = text.lower() # нижний регистр всех слов

# удаление лишних символов
#bad_chars = list('.,?!-<>\\()1234567890№')
bad_chars = '.,?!;:/|-+<>\\[]\()1234567890№"\''
for i in bad_chars:
    text = text.replace(i, ' ')


text_split = text.split() # список из отдельных слов

split_list = [] # создан пустой список уникальных слов

# формирование списка уникальных слов
for i in text_split:
    if i not in split_list:
        split_list.append(i)

count_list = [] # создан пустой список слов с указанием их количества
word_count_list = '' # создано пустая строка для присваивания количества вхождения каждого слова

# формирование списка с добавлением количества их вхождения в первоначальном тексте
for i in split_list:
    if i not in count_list:
        word_count_list = str(text.count(i)) + ' - ' + i
        count_list.append(word_count_list)

count_list.sort(reverse=True) # сортировка списка

word_count = ''
for i in count_list:
    if i not in word_count:
        word_count = word_count + '\n' + i

print(word_count)

input()
