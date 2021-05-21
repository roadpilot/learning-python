#!/usr/bin/env python3

x = 'seven {} {}'.format(8, 9)
x = 'seven {1} {0}'.format(8, 9)
x = 'seven {1:<9} {0:>9}'.format(8, 9)
x = 'seven "{1:<09}" "{0:>09}"'.format(8, 9)
a = 8
b = 9
x = f'seven {a} {b}'

print('x is {}'.format(x))
print(type(x))