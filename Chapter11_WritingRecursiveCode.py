def get_total_number_of_characters(array_of_strings):
    if len(array_of_strings) == 1:
        return len(array_of_strings[0])

    return len(array_of_strings[0]) + get_total_number_of_characters(array_of_strings[1:])


def get_array_of_even_numbers(array_of_numbers):
    array_of_even_numbers = []

    if (array_of_numbers[0] % 2) == 0:
        array_of_even_numbers.append(array_of_numbers[0])

    if len(array_of_numbers) == 1:
        return array_of_even_numbers

    return array_of_even_numbers + get_array_of_even_numbers(array_of_numbers[1:])


def get_triangular_number(number_of_the_sequence):
    if number_of_the_sequence == 1:
        return 1

    return number_of_the_sequence + get_triangular_number(number_of_the_sequence - 1)


def get_index_of_first_x(string_to_verify, current_index_in_string=0):
    if string_to_verify[current_index_in_string] == 'x':
        return current_index_in_string
    else:
        current_index_in_string += 1
        return get_index_of_first_x(string_to_verify, current_index_in_string)


def main():
    print("Total number of character of the array is:", get_total_number_of_characters(["ab", "c", "def", "ghji"]))
    print("Even numbers of the array is:", get_array_of_even_numbers([1, 2, 3, 4, 5, 6]))
    print("Value for triangular number is:", get_triangular_number(7))
    print("Index of first x in the string is:", get_index_of_first_x("abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
