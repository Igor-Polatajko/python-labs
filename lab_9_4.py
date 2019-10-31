#!/usr/bin/env python

CONVERT_DICT = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M',
    2000: 'MM',
    3000: 'MMM'
}


def invert_dict(dictionary):
    return {v: k for k, v in dictionary.items()}


def _is_in_bounds_arabic(arabic_number):
    return 0 <= int(arabic_number) < 4000


def _is_in_bounds_roman(roman_number):
    thousand_symbol = 'M'
    thousand_count = 0
    thousand_count_allowed = 3
    for sym in roman_number:
        if sym == thousand_symbol:
            thousand_count += 1
    return thousand_count <= thousand_count_allowed


def _convert_to_roman(arabic_number):
    multiplier = 1
    roman_number = ''
    for d in arabic_number[::-1]:
        if int(d) != 0:
            roman_number += CONVERT_DICT[int(d) * multiplier][::-1]
        multiplier *= 10
    return roman_number[::-1]


def _convert_to_arabic(roman_number):
    sequence_rule = 'IVXLCDM'
    arabic_number = 0
    convert_dict = invert_dict(CONVERT_DICT)

    previous_symbol = None
    temp_sum = 0
    for s in roman_number:
        if s not in sequence_rule:
            raise ValueError
        temp_sum += convert_dict[s]

        if previous_symbol and sequence_rule.find(s) < sequence_rule.find(previous_symbol):
            arabic_number -= temp_sum
        else:
            arabic_number += temp_sum
        previous_symbol = s

    return arabic_number


def convert(number_data):
    handler = number_data['handler']
    return handler(number_data['number'])


def fetch_number_data(user_input):
    for i in user_input:
        if not str(i).isdigit():
            break
    else:
        return {'validator': _is_in_bounds_arabic, 'handler': _convert_to_roman, 'number': user_input}

    for i in user_input:
        if i not in ('I', 'V', 'X', 'L', 'C', 'M'):
            break
    else:
        return {'validator': _is_in_bounds_roman, 'handler': _convert_to_arabic, 'number': user_input}

    raise ValueError


def main():
    user_input = input("Enter number: ")
    try:
        number_data = fetch_number_data(user_input)
        validator = number_data['validator']
        if not validator(number_data['number']):
            print("Number out of bounds")
            raise ValueError
        print(convert(number_data))
    except ValueError:
        print("Incorrect input!")


if __name__ == '__main__':
    main()
