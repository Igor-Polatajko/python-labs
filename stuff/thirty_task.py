#!/usr/bin/env python


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


def calc_recommended_views_for_buys_count(buys_count, a_coef, b_coef):
    return (buys_count - b_coef) // a_coef


def main():
    views = [5250, 7620, 940, 1160, 480, 300, 240, 195, 150, 140]
    buys = [21, 46, 9, 8, 3, 6, 4, 2, 2, 2]
    a_coef = calc_a(views, buys)
    b_coef = calc_b(a_coef, views, buys)
    def_test_value = 30
    print(f"Recommended views count for {def_test_value} buys: "
          f"{calc_recommended_views_for_buys_count(def_test_value, a_coef, b_coef)}")


if __name__ == '__main__':
    main()
