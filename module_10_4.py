import threading
import time
from random import randint
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name #Имя гостя
    def run(self):
        time.sleep(randint(7,20))


class Cafe:

    def __init__(self, *table):
        self.tables = table
        self.queue = Queue()
    def guest_arrival(self, *guests): # прибытие гостей
        for i in range(len(guests)): # проверка стола на занятость
            if i < len(self.tables):
                if self.tables[i].guest == None:
                    self.tables[i].guest = guests[i] # ожидание
                    print(f"{guests[i].name} сел(-а) за стол номер {self.tables[i].number}")
                    guests[i].start()
            else:
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self): #обслужить гостей
        is_true = False
        while True:
            if is_true:
                break
            for table in self.tables:
                if table.guest != None:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                if table.guest == None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start()
                if self.queue.empty():
                    for i in self.tables:
                        if i.guest == None:
                            is_true = True
                        else:
                            is_true = False
                            break

tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей

guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()