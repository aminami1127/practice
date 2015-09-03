# -*- coding:utf-8 -*-

def infinite_generator(start):
    """startからの数を2乗した数を無限に返すIterator"""
    while True:
        yield start ** 2
        start += 1

sample = infinite_generator(1)
for i in sample:
    print(i)
    if i > 1000:
        break
