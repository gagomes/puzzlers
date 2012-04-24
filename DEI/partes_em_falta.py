#!/usr/bin/python

import sys

all = [ [a,b,c] for a in range(1,4) for b in range(1,4) for c in range(1,4) ] 
new = []
while 1:
    l = sys.stdin.readline ()
    if "-1" in l:
        break
    new.append(map(int, l.split()))

all = [n for n in all if n not in new]

sys.stdout.write (''.join(
        [" ".join(map(str,n))+"\n" for n in all]))
