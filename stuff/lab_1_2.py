#!/usr/bin/env python

from math import floor
from math import sqrt
from random import randint


# lab 1
def calc_mode(input_list):
    return max(set(input_list), key=input_list.count)


# lab 1
def calc_median(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) % 2:
        return input_list[floor(len(sorted_list) / 2)]
    return (input_list[int(len(sorted_list) / 2 - 1)] + input_list[int(len(sorted_list) / 2)]) / 2


# lab 1
def calc_avg(input_list):
    return sum(input_list) / len(input_list)


# lab 1
def calc_disp(input_list):
    square_list = list(map(lambda x: x ** 2, input_list))
    return calc_avg(square_list) - calc_avg(input_list) ** 2


# lab 1
def quadratic_deviation(input_list):
    return sqrt(calc_disp(input_list))


# lab 1
def random_list():
    lower_bound = randint(-100, 100)
    upper_bound = randint(lower_bound, 100)
    length = randint(0, 100)
    rand_list = []
    [rand_list.append(randint(lower_bound, upper_bound)) for _ in range(length)]
    return rand_list


# lab 2
def calc_scope(input_list):
    return max(input_list) - min(input_list)


# lab 2
def calc_iqr(input_list):
    sorted_list = sorted(input_list)
    half_len = floor((len(sorted_list)) / 2)
    q1 = calc_median(sorted_list[0:half_len])
    second_part_start_index = half_len + 1 if len(sorted_list) % 2 else half_len
    q2 = calc_median(sorted_list[second_part_start_index:len(sorted_list)])
    return q2 - q1


if __name__ == '__main__':
    test_data = [1, 22, 5, 22, 1, 3, 6, 22]
    print(f"Test data: {test_data}")
    print(f"Mode: {calc_mode(test_data)}")
    print(f"Median: {calc_median(test_data)}")
    print(f"Average: {calc_avg(test_data)}")
    print(f"Dispersion: {calc_disp(test_data)}")
    print(f"Quadratic deviation: {quadratic_deviation(test_data)}")
    print(f"Sorted: {sorted(test_data)}")
    print(f"Random list: {random_list()}")
    print(f"Scope: {calc_scope(test_data)}")
    print(f"IQR: {calc_iqr(test_data)}")
