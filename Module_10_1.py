# Импорты необходимых модулей и функций
import datetime
import threading
import time


# Объявление функции write_words
def write_words(word_count, file_name):
    f = open(file_name, 'w')
    f.close()
    for i in range(1, word_count + 1):
        file = open(file_name, 'a', encoding='utf-8')
        file.write('Какое-то слово №' + str(i) + '\n')
        time.sleep(0.1)
        file.close()
    print(f'Завершилась запись в файл {file_name}')


# Взятие текущего времени
now = datetime.datetime.now()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
now_2 = datetime.datetime.now()

# Вывод разницы начала и конца работы функций
time_diff = now_2 - now
print(f'Работа потоков: {time_diff}')

# Взятие текущего времени
now_3 = datetime.datetime.now()

# Создание и запуск потоков с аргументами из задачи
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

# Взятие текущего времени
now_4 = datetime.datetime.now()

# Вывод разницы начала и конца работы потоков
time_diff2 = now_4 - now_3
print(f'Работа потоков: {time_diff2}')
