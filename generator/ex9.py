# -*- coding:utf-8 -*-

def send_value_generator():
    """generatorの呼び出し時に値を送るサンプル"""
    i = (yield)  # i = 1が代入される
    while True:
        # sendされた値がiに設定された後、i ** 2がyieldされる
        i = (yield i ** 2)


sample = send_value_generator()
next(sample)
print(sample.send(1))
print(sample.send(2))
print(sample.send(3))
print(sample.send(4))
print(sample.send(5))
