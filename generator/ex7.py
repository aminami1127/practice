# -*- coding:utf-8 -*-

class EvenOddIterator(object):
    """呼び出された回数が奇数か偶数かを返すIterator"""
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    # python3 => __next__(self):
    def next(self):
        self.i += 1
        while True:
            if self.i % 2:
                return 'odd'
            else:
                return 'even'
            # generatorと違いreturnの後に処理を書けない

sample = EvenOddIterator()
for i, x in enumerate(sample):
    print(x)
    if i > 1000:
        break
