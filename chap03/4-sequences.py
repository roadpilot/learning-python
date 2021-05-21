#!/usr/bin/env python3

x = 7 
x = 7 * 3
x = 7.0
x = 7 * 3.14
x = 7 / 3
x = 7 // 3
x = 7 % 3
x = .1 + .1 + .1 - .3

from decimal import *
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b

print('x is {}'.format(x))
print(type(x))