#!/usr/bin/env python3

import platform

x = 42

def main():
    message()

def message():
    print(f'Hello, World. {x}') #python3.6+
    print('Hello, World. {}'.format(x)) #python3+
    print('Hello, World. %d' % x) #python2

if __name__ == '__main__': main()