import pyperclip

file = open(r'Текст.txt', 'r', encoding='utf8')
text = file.read()

text = text.lower()
choice = int(input('Введите:\nДля преобразования "ОФЕРТ" -------- >>> 1 <<<\nДля преобразования "ID" ----------- >>> 2 <<<\nДля преобразования другого текста - >>> 3 <<<\n'))
print('')
text_list = set(text.split())
text_list = sorted(list(text_list))
text_new = []


for i in text_list:
    if choice == 1:
        if 'оф-2020-' not in i:
            i = 'оф-2020-' + i
            text_new.append(i)
        elif 'оф-2020-' in i:
            text_new.append(i)
    elif choice == 2:
        if 'т' not in i:
            i = 'т' + i
            text_new.append(i)
        elif 'т' in i:
            text_new.append(i)
    elif choice == 3: #просто соеденялка
        text_new.append(i)
        
       
text = '|'.join(text_new)
count = 1
for i in text_new:
    if len(str(count)) == 1:
        print(count, '   ', i, sep = '')
    elif len(str(count)) == 2:
        print(count, '  ', i, sep = '')
    else:
        print(count, ' ', i, sep = '')
    count +=1

pyperclip.copy(text) #копирование текста в буфер обмена

file.close()

input()
