#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
进程之间使用Queue通信
'''

from multiprocessing import Queue, Process
import time
import random

list1 = ['java', 'python', 'js']


def write(queue):
    for value in list1:
        print(f'正在向队列中添加数据-->{value}')
        queue.put_nowait(value)
        time.sleep(1)


def read(queue):
    while True:
        if not queue.empty():
            value = queue.get_nowait()
            print(f'从队列中取出数据为-->{value}')
            time.sleep(1)
        else:
            break


if __name__ == '__main__':
    queue = Queue()
    write_data = Process(target=write, args=(queue,))
    read_data = Process(target=read, args=(queue,))

    write_data.start()
    write_data.join()
    print('*' * 20)
    read_data.start()
    read_data.join()
    print('所有数据都读写完成！')
