#!/usr/bin/env python


def is_power_of_two(number):
    return number & (number - 1) == 0


if __name__ == '__main__':
    try:
        number = int(input("Enter your monthly revenue: "))
        print(number, ("- is" if is_power_of_two(number) else "- is not"), "the power of two")
    except ValueError:
        print("Incorrect input")
