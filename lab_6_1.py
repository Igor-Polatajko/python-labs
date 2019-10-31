#!/usr/bin/env python
from math import sqrt


def calc_triangle_area(side_a, side_b, side_c):
    s = (side_a + side_b + side_c) / 2
    return sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))


def can_triangle_exist(side_a, side_b, side_c):
    return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a


def main():
    try:
        side_a = float(input("Enter side a: "))
        side_b = float(input("Enter side b: "))
        side_c = float(input("Enter side c: "))

        if not can_triangle_exist(side_a, side_b, side_c):
            print("Triangle cannot exist")
            raise ValueError
    except ValueError:
        print("Incorrect input")
    else:
        print(f"Triangle area: {calc_triangle_area(side_a, side_b, side_c)}")


if __name__ == '__main__':
    main()
