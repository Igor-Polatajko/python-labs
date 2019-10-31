#!/usr/bin/env python


def calc_resulting_amount(current_amount, annual_interest_rate, deposit_duration):
    resulting_amount = current_amount
    annual_interest_coef = annual_interest_rate / 100
    for _ in range(0, deposit_duration):
        resulting_amount *= 1 + annual_interest_coef
    return resulting_amount


def main():
    try:
        current_amount = Decimal(input("Enter current amount of money: "))
        annual_interest_rate = Decimal(input("Enter annual interest rate (in %): "))
        deposit_duration = int(input("Enter deposit duration (in years): "))
    except ValueError:
        print("Incorrect input")
    else:
        resulting_amount = calc_resulting_amount(current_amount, annual_interest_rate, deposit_duration)
        print(f"Resulting amount: {resulting_amount}")


if __name__ == '__main__':
    main()
