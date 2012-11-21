#!/usr/bin/python

def isPrime(n):
    if n == 1:
        return 0
    else:
        for x in range(2,int(n**0.5)+1):
            if n%x == 0:
                return 0
        return 1

counter = 0
iter = 0

while 1:
    iter += 1
    counter += isPrime(iter)

    if counter == 10001:
        print "The 10,001 prime is %d" % iter
        break
