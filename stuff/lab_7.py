#!/usr/bin/env python
import math

import matplotlib.pyplot as plt
import numpy as np


def calc_groups_number(data_len):
    return round(1 + 3.322 * math.log10(data_len))


def calc_interval_width(data):
    return (max(data) - min(data)) / calc_groups_number(len(data))


def divide_on_periods(data):
    data.sort()
    interval_width = calc_interval_width(data)
    result = []
    period_start = min(data)

    while period_start <= max(data):
        period_end = round(period_start + interval_width, 3)
        result.append(({
            'interval': [period_start, period_end],
            'elements': list(filter(lambda x: period_start <= x < period_end, data))}))
        period_start = period_end

    return result


def calc_mode(input_list):
    return max(set(input_list), key=input_list.count)


def calc_median(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) % 2:
        return input_list[math.floor(len(sorted_list) / 2)]
    return (input_list[int(len(sorted_list) / 2 - 1)] + input_list[int(len(sorted_list) / 2)]) / 2


def calc_interval_row(data):
    divided_data = divide_on_periods(data)
    result_data = []

    fic = 0
    wic = 0
    for d in divided_data:
        row = dict()
        els = d['elements']
        row['interval'] = d['interval']
        row['middle'] = round((d['interval'][1] + d['interval'][0]) / 2, 2)
        row['fi'] = round(len(els), 2)
        row['wi'] = round(len(els) / len(data), 2)
        fic += row['fi']
        wic += row['wi']
        row['fic'] = round(fic, 2)
        row['wic'] = round(wic, 2)
        row['mo'] = calc_mode(els)
        row['me'] = calc_median(els)
        row['data'] = els
        result_data.append(row)

    return result_data


def get_max_len_by_key(data, key):
    return max(list(map(lambda el: len(str(el[key])), data)) + [len(key)])


def draw_table(data):
    if len(data) < 1:
        print("#### Empty table! ####")
        return

    keys = data[0].keys()
    for key in keys:
        print(f"{key.capitalize():<{get_max_len_by_key(data, key)}} | ", end='')
    print()

    for d in data:
        for key in keys:
            print(f"{str(d[key]):<{get_max_len_by_key(data, key)}} | ", end='')
        print()


def draw_plot(raw_data, data):
    x_lower = [min(row['data']) for row in data]
    wic = [(row['wic']) for row in data]
   # plt.plot(x_lower, wic)
    plt.hist(raw_data, bins=len(data), density=True)
    plt.show()


def calc_average(data):
    return sum([d['fi'] * d['middle'] for d in data]) / sum([d['fi'] for d in data])


def calc_coefs(raw_data, data):
    xi_fi = [d['fi'] * d['middle'] for d in data]

    xa_weight = sum(xi_fi) / len(raw_data)
    product_2 = []
    product_3 = []
    product_4 = []
    for i in range(0, len(data)):
        product_2.append(((data[i]['middle'] - xa_weight) ** 2) * data[i]['fi'])
        product_3.append(((data[i]['middle'] - xa_weight) ** 3) * data[i]['fi'])
        product_4.append(((data[i]['middle'] - xa_weight) ** 4) * data[i]['fi'])
    d = sum(product_2) / len(raw_data)
    sigma = math.sqrt(d)
    m3 = sum(product_3) / len(raw_data)
    m4 = sum(product_4) / len(raw_data)
    return {'asymmetry': round(m3 / sigma ** 3, 3),
            'excess': round((m4 / sigma ** 4) - 3, 3)}


def main():
    data = [4.21, 5.22, 2.84, -0.2, 6.37, -0.54, -3.71, 2.77,
            6.35, 5.88, 3.99, -1.25, -4.38, -3.5, -2.4, 4.51,
            -1.43, -4.47, 4.01, 5.33, 2.61, 3.8, 2.35, -2.59,
            -2.16, 2.06, -2.13, 3.03, 6.59, 2.13]
    data = np.random.normal(110, 18, 1000)
    result_data = calc_interval_row(data)

    draw_table(result_data)
    print(f"Average: {calc_average(result_data)}")
    coefs = calc_coefs(data, result_data)
    print(f"Asymmetry coefficient: {coefs['asymmetry']}")
    print(f"Excess coefficient: {coefs['excess']}")
    draw_plot(data, result_data)


if __name__ == '__main__':
    main()
