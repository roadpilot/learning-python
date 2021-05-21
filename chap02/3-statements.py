#!/usr/bin/env python3

import platform

version = platform.python_version()

def main():
    message()

def message():
    print('This is python version {}'.format(version))    
    print('hello')
    if True:
        print('true')
    else:
        print('false')
#comment
#comment
#comment
#comment
#comment
#comment
#comment
if __name__ == '__main__': main()