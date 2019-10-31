#!/usr/bin/env python
from matplotlib import pyplot as plt


def calc_avg(input_list):
    return sum(input_list) / len(input_list)


def calc_disp(input_list):
    square_list = list(map(lambda x: x ** 2, input_list))
    return calc_avg(square_list) - calc_avg(input_list) ** 2


def calc_a(x_list, y_list):
    xy_list = list(map(lambda x, y: x * y, x_list, y_list))
    return (calc_avg(xy_list) - calc_avg(x_list) * calc_avg(y_list)) / calc_disp(x_list)


def calc_b(a_coef, x_list, y_list):
    return calc_avg(y_list) - a_coef * calc_avg(x_list)


def calc_least_squares_line(a_coef, b_coef, x_list):
    return list(map(lambda x: a_coef * x + b_coef, x_list))


def draw_plots(x_list, y_list, lsl):
    plt.scatter(x_list, y_list)
    plt.plot(x_list, lsl, color='tab:red')
    plt.show()


# variant 19
def main():
    x_list = [1, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8, 3.1, 3.4, 3.7, 4.0, 4.3, 4.6, 4.9, 5.2]
    y_list = [0.5, 0.5, 0.6, 0.6, 0.7, 0.8, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8]
    assert len(x_list) == len(y_list)
    a_coef = calc_a(x_list, y_list)
    b_coef = calc_b(a_coef, x_list, y_list)
    lsl = calc_least_squares_line(a_coef, b_coef, x_list)

    draw_plots(x_list, y_list, lsl)


if __name__ == '__main__':
    main()
