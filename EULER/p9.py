#!/usr/bin/python
'''
Good candidate for optimization.
timed on my computer:

real	0m34.708s
user	0m34.664s
sys	0m0.024s
'''

def is_ptriangle(a, b, c):
    return (a < b < c) and ((a ** 2) + (b ** 2) == (c ** 2))

def main():
    for a in range(0, 1000):
        for b in range(0, 1000):
            for c in range(0, 1000):
                if is_ptriangle(a,b,c) and (a + b + c) == 1000:
                    return print(a * b * c)


if __name__ == '__main__':
    main()
