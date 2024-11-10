import threading
from threading import Thread
import time

# Создание класса
class Knight(threading.Thread):
    def __init__(self, name, power, counter=1, all_=100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter = counter
        self.all_ = all_

    def run(self):
        print(f'{self.name}, на нас напали!')
        amount = self.all_
        count_1 = self.counter
        while amount > self.power:
            time.sleep(1)
            print(f'{self.name} сражается {count_1} день, осталось {amount - self.power} воинов.')
            amount = amount - self.power
            count_1 = count_1 + 1

        print(f'{self.name} одержал победу спустя {self.all_ / self.power} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print(f'Все битвы закончились!')
