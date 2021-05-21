#!/usr/bin/env python3

import platform

x = 42
y = 73

def main():
    message()

def message():
    z = 112
    if x > y:
        print('x < y: x is {} and y is {}'.format(x, y))
        print('another line')
        print('another line')
        print('another line')
        print('another line')
        #indentation identifies block members
    elif x == y:
        print('something else')
    else:
        print('something else')
    print(f'z is {z}')

if __name__ == '__main__': main()