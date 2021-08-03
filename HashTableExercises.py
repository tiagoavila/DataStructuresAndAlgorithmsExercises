import string


def get_intersection_of_arrays(array1, array2):
    array1_as_dictionary = {}
    intersection_array = []

    for item in array1:
        array1_as_dictionary[item] = True

    for item2 in array2:
        if item2 in array1_as_dictionary:
            intersection_array.append(item2)

    print('Intersection Array:', intersection_array)


def get_first_duplicate_value_in_string(array_of_characters):
    dictionary_of_characters = {}

    for character in array_of_characters:
        if character in dictionary_of_characters:
            print('First duplicated character is:', character)
            break
        else:
            dictionary_of_characters[character] = True


def get_missing_letter(phrase):
    phrase_dictionary = dict.fromkeys(phrase.replace(" ", ""), True)

    for character in 'abcdefghijklmnopqrstuvwxyz':
        if not phrase_dictionary.get(character):
            print('Missing letter from alphabet is:', character)
            break


def get_first_non_duplicated_character(my_string):
    my_string_as_dictionary = {}

    for character in my_string:
        if not my_string_as_dictionary.get(character):
            my_string_as_dictionary[character] = 1
        else:
            my_string_as_dictionary[character] += 1

    for key in my_string_as_dictionary:
        if my_string_as_dictionary[key] == 1:
            print('First non duplicated character is:', key)
            break


def main():
    get_intersection_of_arrays([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])
    get_first_duplicate_value_in_string(["a", "b", "c", "d", "c", "e", "f"])
    get_missing_letter("the quick brown box jumps over a lazy dog")
    get_first_non_duplicated_character("minimum")


if __name__ == "__main__":
    main()
