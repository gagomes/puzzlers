def main():
    i = 1
    while not all([i % n == 0 for n in range(1, 20)]):
        i += 1
    print(i)

if __name__ == '__main__':
    main()
