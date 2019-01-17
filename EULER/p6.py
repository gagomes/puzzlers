def main():
    sum_sq = sum([n ** 2 for n in range(1, 101)])
    sq_sum = sum([n for n in range(1, 101)]) ** 2

    print(sq_sum - sum_sq)

if __name__ == '__main__':
    main()