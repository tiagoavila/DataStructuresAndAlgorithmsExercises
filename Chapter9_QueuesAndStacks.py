def reverse_string(my_string):
    stack = []
    reversed_string = ""

    for character in my_string:
        stack.append(character)

    for character in my_string:
        reversed_string += stack.pop()

    print(reversed_string)


def main():
    reverse_string("abcde")


if __name__ == "__main__":
    main()