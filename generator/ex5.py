# -*- coding:utf-8 -*-
import itertools

# startからの数を2乗した数を無限に返すgenerator
infinite_generator = lambda x: (y ** 2 for y in itertools.count(x))

sample = infinite_generator(1)
for i in sample:
    print(i)
    if i > 1000:
        break
