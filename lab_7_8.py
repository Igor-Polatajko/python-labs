#!/usr/bin/env python


def print_sequence(first, last):
    for i in range(first, last + 1):
        res = ''
        if i % 3 == 0:
            res += 'Fizz'
        if i % 5 == 0:
            res += 'Buzz'

        if res == '':
            res = i
        print(res)


if __name__ == '__main__':
    print_sequence(1, 100)
