#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time


def func1():
    for i in range(11):
        yield
        print(f'这是我第{i}次打印')
        time.sleep(1)


def func2():
    g = func1()
    next(g)
    for k in range(10):
        print(f'哈哈，我第{k}次打印啦！')
        time.sleep(1)
        next(g)


if __name__ == '__main__':
    func1()
    func2()
