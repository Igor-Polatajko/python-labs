#!/usr/bin/env python
from decimal import Decimal


def calc_deposit_duration(current_amount, required_amount, annual_interest_rate):
    result_duration = 0
    annual_interest_coef = annual_interest_rate / 100
    while current_amount < required_amount:
        required_amount /= 1 + annual_interest_coef
        result_duration += 1
    return result_duration


def main():
    try:
        current_amount = Decimal(input("Enter current amount of money: "))
        required_amount = Decimal(input("Enter required amount of money: "))
        annual_interest_rate = Decimal(input("Enter annual interest rate (in %): "))
    except ValueError:
        print("Incorrect input")
    else:
        resulting_duration = calc_deposit_duration(current_amount, required_amount, annual_interest_rate)
        print(f"Deposit duration: {resulting_duration}")


if __name__ == '__main__':
    main()
