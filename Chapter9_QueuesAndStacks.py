def reverse_string(my_string):
    queue = []
    reversed_string = ""

    for character in my_string:
        queue.append(character)

    for character in my_string:
        reversed_string += queue.pop()

    print(reversed_string)


def main():
    reverse_string("abcde")


if __name__ == "__main__":
    main()