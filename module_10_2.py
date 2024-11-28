import threading, time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        count = 0
        while enemies != 0:
            enemies -= self.power
            time.sleep(1)
            count += 1
            print(f'{self.name} сражается {count} день(дня), осталось {enemies} воинов')
        if enemies == 0:
            print(f'{self.name} одержал победу спустя {count} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения