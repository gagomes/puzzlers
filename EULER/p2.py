#!/usr/bin/python

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

even = []

n = 1
while 1:
    f = fib(n)
    if f % 2 == 0:
        even.append(f)
    if f >= 4000000:
        break
    n += 1

print sum(even)
