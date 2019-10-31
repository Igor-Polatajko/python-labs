#!/usr/bin/env python


def calc_roots(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d == 0:
        result = [(-b) / (2 * a)]
    else:
        sqrt_d = d ** 0.5
        result = [((-b - sqrt_d) / (2 * a)), ((-b + sqrt_d) / (2 * a))]
    return result


def main():
    print("a * x^2 + b * x + c = 0")
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        result = calc_roots(a, b, c)
        print(("Roots:" if len(result) == 2 else "Root:"), result)
    except ValueError:
        print("Incorrect input!")


if __name__ == '__main__':
    main()
