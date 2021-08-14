def add_until_100(array):
    if len(array) == 0:
        return 0

    sum_rest_array = add_until_100(array[1:])

    if array[0] + sum_rest_array > 100:
        return sum_rest_array

    return array[0] + sum_rest_array


def golomb(n, memo={}):
    if n == 1:
        return 1

    memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)

    return memo[n]


def main():
    print("Add until 100:", add_until_100([1, 2, 3, 4, 5, 6, 100, 9]))
    print("Golomb of 10 is 5:", golomb(10))
    print("Golomb of 8 is 4:", golomb(8))
    print("Golomb of 7 is 4:", golomb(7))
    print("Golomb of 5 is 3:", golomb(5))
    print("Golomb of 3 is 2:", golomb(3))


if __name__ == "__main__":
    main()