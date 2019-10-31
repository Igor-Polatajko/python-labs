#!/usr/bin/env python


def count_gen():
    count = 0

    while True:
        count += 1
        yield count


def calc_fun(count_gen):
    return count_gen.__next__()


if __name__ == '__main__':
    count_gen_obj = count_gen()
    for i in range(0, 15):
        print(calc_fun(count_gen_obj))
