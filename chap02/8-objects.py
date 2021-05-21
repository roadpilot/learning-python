#!/usr/bin/env python3

class Duck:
    # class variables
    sound = 'Quack'
    walking = 'Walks like a duck.'
    def quack(self): # reference to instance of object created
        print('Quaaack!')
        print(self.sound)

    def walk(self):
        print('Walks like a duck.')
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()