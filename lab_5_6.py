#!/usr/bin/env python


def can_triangle_exist(a, b, c):
    return a + b > c and a + c > b and b + c > a


if __name__ == '__main__':
    try:
        a = float(input("Enter length of 'a' side of triangle: "))
        b = float(input("Enter length of 'b' side of triangle: "))
        c = float(input("Enter length of 'c' side of triangle: "))
        print("Such triangle", ("can" if can_triangle_exist(a, b, c) else "cannot"), "exist")
    except ValueError:
        print("Incorrect input")
