#!/usr/bin/env python
from math import floor


def calc_avg(data):
    return sum(data) / len(data)


def calc_median(data):
    data = sorted(data)
    if len(data) % 2:
        return data[floor(len(data) / 2)]
    return (data[int(len(data) / 2)] + data[(int(len(data) / 2)) - 1]) / 2


if __name__ == '__main__':
    data1 = [1, 22, 15, 3, 19, 55, -5, 78, -65, 33, -33]
    data2 = [16, 22, 19, 3, 19, 5, 4, 8, -3, 6]
    print(f"First dataset: {data1}")
    print(f"Average: {calc_avg(data1)}")
    print(f"Median: {calc_median(data1)}")
    print(f"Second dataset: {data2}")
    print(f"Average: {calc_avg(data2)}")
    print(f"Median: {calc_median(data2)}")
