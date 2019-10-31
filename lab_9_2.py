#!/usr/bin/env python
from math import floor

NUMBERS = {
    0: 'нуль',
    1: 'одна',
    2: 'дві',
    3: 'три',
    4: 'чотири',
    5: 'п\'ять',
    6: 'шість',
    7: 'сім',
    8: 'вісім',
    9: 'дев\'ять',
    10: 'десять',
    11: 'одинадцять',
    12: 'дванадцять',
    13: 'тринадцять',
    14: 'чотирнадцять',
    15: 'п\'ятнадцять',
    16: 'шістнацять',
    17: 'сімнадцять',
    18: 'вісімнадцять',
    19: 'дев\'ятнадцять',
    20: 'двадцять',
    30: 'тридцять',
    40: 'сорок',
    50: 'п\'ятдесят',
    60: 'шістдесят',
    70: 'сімдесят',
    80: 'вісімдесят',
    90: 'дев\'яносто',
    100: 'сто',
    200: 'двісті',
    300: 'триста',
    400: 'чотириста',
    500: 'п\'ятсот',
    600: 'шістсот',
    700: 'сімсот',
    800: 'вісімсот',
    900: 'дев\'ятсот',
}


def resolve_pronunciation(number):
    def _decide_by_number(n):
        if n == 1:
            return {'uah': 'гривня', 'coin': 'копійка', 'thousand': 'тисяча'}
        if n in (2, 3, 4):
            return {'uah': 'гривні', 'coin': 'копійки', 'thousand': 'тисячі'}
        return {'uah': 'гривень', 'coin': 'копійок', 'thousand': 'тисяч'}

    if number in (1, 2, 3, 4):
        return _decide_by_number(number)
    if number in NUMBERS.keys():
        return {'uah': 'гривень', 'coin': 'копійок', 'thousand': 'тисяч'}

    last = int(str(number)[-1])
    if len(str(number)) > 1:
        before_last = int(str(number)[-2])
        if before_last == 1:
            last = int(str(last) + str(before_last))
    return _decide_by_number(last)


def get_integer_parts(number):
    parts = number.split('.')
    if len(parts) == 1:
        parts.append('0')
    parts[1] = parts[1][0:2]
    if len(parts[1]) == 1:
        parts[1] += '0'
    assert len(parts) == 2
    return dict(zip(['uah', 'coin'], list(map(lambda p: int(p), parts))))


def perform_advanced_resolving(number):
    result = ''
    multiplier = 1
    processing_of_last = True

    while number >= 1:
        if multiplier == 1000:
            multiplier = 1
            processing_of_last = True
            result += ' ' + resolve_pronunciation(floor(number))['thousand']

        number_coef = 10
        multiplier_coef = 10

        if number % 10 != 0:
            if 10 < number % 100 < 20 and processing_of_last:
                number_last_part = number % 100
                number_coef = 100
                multiplier_coef = 100
            else:
                number_last_part = number % 10
            result += ' ' + integer_part_convert(number_last_part * multiplier)
        multiplier *= multiplier_coef
        number = floor(number / number_coef)
        processing_of_last = False

    return ' '.join(reversed(result.split()))


def integer_part_convert(number):
    if number in NUMBERS.keys():
        return NUMBERS[number]
    return perform_advanced_resolving(number)


def to_written_form(amount_parts):
    result = f"{integer_part_convert(amount_parts['uah'])} \
{resolve_pronunciation(amount_parts['uah'])['uah']}"
    if amount_parts['coin'] != 0:
        result += f" {integer_part_convert(amount_parts['coin'])} \
{resolve_pronunciation(amount_parts['coin'])['coin']}"
    return result


def main():
    try:
        amount_str = input("Введіть суму: ")
        if float(amount_str) > 999999.99:
            print("Сума перевищує максимальну")
            raise ValueError

        if float(amount_str) < 0:
            print("Сума не може бути меншою за нуль")
            raise ValueError

        parts = get_integer_parts(amount_str)
    except ValueError or AssertionError:
        print("Некоректий ввід!")
    else:
        print(f"Письмова форма запису: {to_written_form(parts)}")


if __name__ == '__main__':
    main()
