# -*- coding:utf-8 -*-

def sample_generator(start, end):
    """startからendまでの数を2乗して返すgenerator"""
    for i in range(start, end + 1):
        yield i ** 2

sample = sample_generator(1, 10)  # generatorを呼び出すとiteratorオブジェクトが返される
print([x for x in sample])
