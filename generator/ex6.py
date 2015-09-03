# -*- coding:utf-8 -*-

def even_odd_generator():
    """呼び出された回数が奇数か偶数かを返すgenerator"""
    # 呼び出された回数を記憶
    # => generatorは状態を持たせることもできる
    i = 1
    while True:
        if i % 2:
            yield 'odd'
        else:
            yield 'even'
        # generatorではyieldした後の処理も次の呼び出しで実行される
        i += 1

sample = even_odd_generator()
for i, x in enumerate(sample):
    print(x)
    if i > 1000:
        break
