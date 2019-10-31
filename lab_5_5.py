#!/usr/bin/env python


def is_prime(num):
    try:
        num = int(num)
    except ValueError:
        return False

    if num <= 1:
        return False

    divisor = num - 1
    while divisor > 1:
        if num % divisor == 0:
            return False
        divisor -= 1
    return True


if __name__ == '__main__':
    number = input("Enter number: ")
    print("Number", ("is" if is_prime(number) else "is not"), "prime")
