from threading import Thread,Lock
import random
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        random_summ = random.randint(50, 500)
        for i in range(100):
            with self.lock:
                self.balance = self.balance + random_summ
                print(f"Пополнение: {random_summ}. Баланс:{self.balance}")

            if self.balance >= 500 and self.lock.locked():
               self.lock.release()


        time.sleep(0.001)

    def take(self):
        random_summ = random.randint(50, 500)
        for i in range(100):
            print(f"Запрос на: {random_summ}")
            with self.lock:
                if random_summ <= self.balance:
                    self.balance -= random_summ
                    print(f"Снятие: {random_summ}. Баланс:{self.balance}")
            if random_summ >= self.balance:
               self.lock.acquire()
               print(f"Запрос отклонен, недостаточно средств")




bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')