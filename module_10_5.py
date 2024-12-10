import multiprocessing
import time

def read_info(name):
    all_data = list()
    with open(name) as file:
        for i in file:
            if file.readline() == '':
                break
            all_data.append(file.readline())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# time1_start = time.time()
# for i in filenames:
#     read_info(i)
# time1_end = time.time()
# Многопроцессный
time2_start = time.time()
if __name__ == '__main__':
    with multiprocessing.Pool(4) as p:
        p.map(read_info, filenames)
# print(time1_end - time1_start, '(линейный)')
time2_end = time.time()
print(time2_end - time2_start, '(многопроцессный)')