#!/usr/bin/env python
from math import *


def get_user_input():
    first_num = float(input("Enter first num: "))
    second_num = float(input("Enter second num: "))
    third_num = float(input("Enter third num: "))
    if third_num == 0:
        raise ValueError
    return first_num, second_num, third_num


def calc_function(first_num, second_num, third_num):
    result = (1 / (third_num * sqrt(2 * pi))) * (exp(-(((first_num - second_num) ** 2)) / 2 * (third_num ** 2)))
    return round(result, 11)


if __name__ == '__main__':
    try:
        first_num, second_num, third_num = get_user_input()
        print(calc_function(first_num, second_num, third_num))
    except ValueError:
        print("Incorrect input")
