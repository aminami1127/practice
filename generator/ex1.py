# -*- coding:utf-8 -*-

class SampleIterator(object):
    """startからendまでの数を2乗して返すIterator"""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    # python3 => __next__(self):
    def next(self):
        if self.start > self.end:
            raise StopIteration
        ret = self.start ** 2
        self.start += 1
        return ret

sample = SampleIterator(1, 10)
print([x for x in sample])
print([x for x in sample])  # もうsampleは要素を返さない

sample = list(SampleIterator(2, 20))  # listにすると要素を全てメモリに格納するため何度も呼び出せる
print([x for x in sample])
print([x for x in sample])

import sys
# sys.maxint
# >> 9223372036854775807
sample = SampleIterator(1, sys.maxint)  # generatorは要素を全てメモリに格納しないためメモリを節約できる
for i in sample:
    print(i)  # １つずつ計算し結果を返す
    if i > 1000:
        break
