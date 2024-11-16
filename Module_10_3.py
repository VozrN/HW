import threading
from threading import Thread, Lock
import random
import time


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.counter = 100
        self.lock = Lock()

    def deposit(self):
        for i in range(self.counter):
            if self.balance >= 500 and self.lock.locked():
                print(self.balance)
                self.lock.release()
            add_balance = random.randint(50, 500)
            self.balance += add_balance
            print(f'Пополнение: {add_balance}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(self.counter):
            withdrawal_balance = random.randint(50, 500)
            print(f'Запрос на {withdrawal_balance}')
            if self.balance < withdrawal_balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= withdrawal_balance
            print(f'Снятие:{withdrawal_balance}. Баланс: {self.balance}')


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
