mail = input('Введите адрес e-mail (полностью)\n')

while '@' and '.' not in mail:
    print('Введён некоректный e-mail')
    mail = input('Введите адрес e-mail (полностью)\n')
else:
    name = mail[:mail.index('@')]
    server = mail[mail.index('@')+1:mail.rindex('.')]
    if server == 'ya':
        server = 'yandex'

    domzona = mail[mail.rindex('.')+1:]
    print('\nЛогин: "', name, '"', sep='')
    print('\nПочтовый сервер: "', server, '"', sep='')
    print('\nДоменная зона: "', domzona, '"', sep='')

print('\n\nСпасибо, что воспользовались данным сервисом.')
input()
