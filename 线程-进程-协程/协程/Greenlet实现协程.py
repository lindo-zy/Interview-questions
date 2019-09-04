#!/usr/bin/python3
# -*- coding:utf-8 -*-

from greenlet import greenlet


def eat(name):
    print(f'{name} eat 1')
    g2.switch('zy')
    print(f'{name} eat 2')
    g2.switch()


def play(name):
    print(f'{name} play 1')
    g1.switch()
    print(f'{name} play 2')


g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch('alice')
