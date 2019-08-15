#!/usr/bin/python3
# -*- coding:utf-8 -*-

import threading
import time

a = threading.local()


def worker():
    a.x = 0
    for i in range(200):
        time.sleep(0.01)
        a.x += 1
    print(threading.current_thread(), a.x)


for j in range(20):
    threading.Thread(target=worker).start()
