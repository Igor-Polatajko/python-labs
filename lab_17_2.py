#!/usr/bin/env python
import math
import operator
import timeit


def bitwise_power(power):
    return 1 << power


def standard_power(power):
    return 2 ** power


def operator_power(power):
    return operator.pow(2, power)


def math_power(power):
    return math.pow(2, power)


def measure_execution_time_power_of_two():
    print("Power of 2:")
    print(f'Bitwise: {timeit.timeit("bitwise_power(12)", setup="from __main__ import bitwise_power")}')
    print(f'Standard: {timeit.timeit("standard_power(12)", setup="from __main__ import standard_power")}')
    print(f'Operator power: {timeit.timeit("operator_power(12)", setup="from __main__ import operator_power")}')
    print(f'Math power: {timeit.timeit("math_power(12)", setup="from __main__ import math_power")}')


def reverse_strings_map(data_list):
    return list(map(lambda string: string[::-1], data_list))


def reverse_strings_comprehension(data_list):
    return [string[::-1] for string in data_list]


def reverse_strings_loop(data_list):
    result = []
    for string in data_list:
        result.append(string[::-1])
    return result


def run_collection_handling(handler):
    data_list = ['123', 'string', 'data', 'python']
    return handler(data_list)


def measure_execution_time_list_handling():
    basic_setup = 'from __main__ import run_collection_handling'
    setup_map = basic_setup + "\nfrom __main__ import reverse_strings_map"
    setup_list_comprehension = basic_setup + "\nfrom __main__ import reverse_strings_comprehension"
    setup_for_loop = basic_setup + "\nfrom __main__ import reverse_strings_loop"
    print("\nReversion of strings in list:")
    print(f'Map: {timeit.timeit("run_collection_handling(reverse_strings_map)", setup=setup_map)}')
    print(f'List comprehension:'
          f' {timeit.timeit("run_collection_handling(reverse_strings_comprehension)", setup=setup_list_comprehension)}')
    print(f'For loop: {timeit.timeit("run_collection_handling(reverse_strings_loop)", setup=setup_for_loop)}')


if __name__ == '__main__':
    measure_execution_time_power_of_two()
    measure_execution_time_list_handling()
