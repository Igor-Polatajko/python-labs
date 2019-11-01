#!/usr/bin/env python


def validate_number(input_number):
    if len(input_number) != 6 or not input_number.isnumeric():
        raise ValueError


def swap_parts(data):
    return data[3:6] + data[0:3]


def multiply(x, y):
    return str(int(x) * int(y))


def retrieve_middle(data):
    for _ in range(0, 12 - len(data)):
        data = '0' + data
    return data[3:9]


def generator(staring_number):
    current_num = staring_number
    while True:
        swapped = swap_parts(current_num)
        current_num = retrieve_middle(multiply(current_num, swapped))
        yield int(current_num)


def main():
    try:
        user_input = input("Enter your number: ")
        iterations_bound = int(input("Enter iterations bound: "))
        validate_number(user_input)
    except ValueError:
        print("Incorrect input!")
    else:
        generator_obj = generator(user_input)
        for _ in range(0, iterations_bound):
            print(generator_obj.__next__())


if __name__ == '__main__':
    main()
