#!/usr/bin/env python3

def function(n = 1): # can set default arg
    print(n)
    return n # this will prevent "None"

function(47)
function() # will return error if no default arg

x = function(42)
print(x) # will return "None" (Null, Nil, etc.)

def isprime(n):
    if n <= 1:
        return False
    for x in range (2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 6
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')

def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=' ', flush=True)
    print()

list_primes()
