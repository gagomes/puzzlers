#!/usr/bin/python

import math

# from stackoverflow
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def main():
    memoize = {}
    sum = 0
    for n in range(2, 2000000):
        if is_prime(n):
            sum += n
            print(sum, n)

    print(sum)


if __name__ == '__main__':
    main()
