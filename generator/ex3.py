# -*- coding:utf-8 -*-

# startからendまでの数を2乗して返すgenerator
sample = lambda x, y: (n ** 2 for n in range(x, y + 1))
print([x for x in sample(1, 10)])
