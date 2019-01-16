#!/usr/bin/python

def main():
    print(sum([n for n in range(1000) if n % 5 == 0 or n % 3 == 0]))
    
if __name__ == '__main__':
    main()

