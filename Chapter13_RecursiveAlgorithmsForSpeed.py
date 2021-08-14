def get_greatest_product_of_3_numbers(array):
    array.sort()

    return array[len(array) - 1] * array[len(array) - 2] * array[len(array) - 3]


def find_missing_number(array):
    array.sort()

    for index in range(len(array)):
        if array[index] != index:
            return index

    return None


def get_greatest_number_in_array_NlogN(array):
    array.sort()

    return array[len(array) - 1]


def get_greatest_number_in_array(array):
    greatest_number = array[0]

    for number in array[1:]:
        if number > greatest_number:
            greatest_number = number

    return greatest_number


def main():
    print("Get greatest product of 3 numbers in array:", get_greatest_product_of_3_numbers([1, 2, 3, 4, 5, 6, 10, 9]))
    print("Missing number is:", find_missing_number([5, 2, 4, 1, 0]))
    print("Greatest number is:", get_greatest_number_in_array_NlogN([5, 2, 4, 7, 1, 0]))
    print("Greatest number is:", get_greatest_number_in_array([9, 2, 4, 17, 1, 0]))


if __name__ == "__main__":
    main()
