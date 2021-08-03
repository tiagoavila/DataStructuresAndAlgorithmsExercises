import string


def get_intersection_of_arrays(array1, array2):
    dictionary_array1 = {}
    intersection_array = []

    for item in array1:
        dictionary_array1[item] = True

    for item2 in array2:
        if item2 in dictionary_array1:
            intersection_array.append(item2)

    print('Intersection Array:', intersection_array)


def get_first_duplicate_value_in_string(array_of_strings):
    dictionary_for_my_string = {}

    for character in array_of_strings:
        if character in dictionary_for_my_string:
            print('First duplicated character is:', character)
            break
        else:
            dictionary_for_my_string[character] = True


def get_missing_letter(phrase):
    phrase_dictionary = dict.fromkeys(phrase.replace(" ", ""), True)
    print(phrase_dictionary)

    for character in 'abcdefghijklmnopqrstuvwxyz':
        if not phrase_dictionary.get(character):
            print('Missing letter from alphabet is:', character)
            break


def get_first_non_duplicated_character(my_string):
    dictionary_for_my_string = {}

    for character in my_string:
        if not dictionary_for_my_string.get(character):
            dictionary_for_my_string[character] = 1
        else:
            dictionary_for_my_string[character] += 1

    print(dictionary_for_my_string)

    for key in dictionary_for_my_string:
        if dictionary_for_my_string[key] == 1:
            print('First non duplicated character is:', key)
            break


def main():
    get_intersection_of_arrays([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])
    get_first_duplicate_value_in_string(["a", "b", "c", "d", "c", "e", "f"])
    get_missing_letter("the quick brown box jumps over a lazy dog")
    get_first_non_duplicated_character("minimum")


if __name__ == "__main__":
    main()
