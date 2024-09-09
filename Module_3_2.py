def send_email(message, recipient, *, sender):
    if ("@",".com",".ru",".net" not in recipient or "@",".com",".ru",".net" not in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


message = input('Введите сообщение для пользователя: ')
recipient = input('Введите адрес отправителя: ')

send_email(message, recipient, sender=input('Введите отправителя: '))
