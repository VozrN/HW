import threading
import time
import datetime
import multiprocessing



def read_info(name):
    all_data = []
    file = open(name, 'r')

    while True:
        line = file.readline()
        if not line:
            break
        all_data.append(line)
    file.close()


if __name__ == '__main__':

    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    now_1 = datetime.datetime.now()
    for i in filenames:
        read_info(i)
    now_2 = datetime.datetime.now()
    time_diff = now_2 - now_1
    print(f'{time_diff} (линейный)')

    # Многопроцессный

    now_3 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    now_4 = datetime.datetime.now()
    time_diff_1 = now_4 - now_3

    print(f'{time_diff_1} (многопроцессорный)')
