#!/usr/bin/python

def is_ptriangle(a, b, c):
    return (a < b < c) and ((a ** 2) + (b ** 2) == (c ** 2))

def main():
    for a in range(0, 1000):
        for b in range(1, 1000):
            for c in range(2, 1000):
                if (a + b + c) == 1000:
                    if is_ptriangle(a, b, c):
                        print(a * b * c)
                        return


if __name__ == '__main__':
    main()
