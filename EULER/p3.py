#!/usr/bin/python

def ispalindrome(n):
    return str(n) == str(n)[::-1]

r1 = range(1000)
r2 = range(1000)

best = 0

for _1 in r1:
    for _2 in r2:
        current = _1 * _2
        if ispalindrome(current):
           best = max(best, current)

print "The largest palindrome is %d" % (best)

