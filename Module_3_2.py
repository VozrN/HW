def send_email(message, recipient, sender='university.help@gmail.com'):
    if ("@" not in recipient or "@" not in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif recipient.endswith(('.com','.net','.ru'))==False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender.endswith(('.com','.net','.ru'))==False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


message = input('Введите сообщение для пользователя: ')
recipient = input('Введите адрес получателя: ')

send_email(message, recipient)
