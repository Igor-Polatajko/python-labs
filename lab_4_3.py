#!/usr/bin/env python
from decimal import Decimal, InvalidOperation

INDIVIDUAL_TAX = Decimal(18)
MILITARY_TAX = Decimal(1.5)


def calc_tax(revenue):
    return revenue * ((INDIVIDUAL_TAX + MILITARY_TAX) / Decimal(100))


if __name__ == '__main__':
    try:
        revenue = Decimal(input("Enter your monthly revenue: "))
        print("Your monthly tax: ", calc_tax(revenue))
    except InvalidOperation:
        print("Incorrect input")
