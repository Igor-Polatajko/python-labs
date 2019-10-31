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

SEQUENCE_RULE = 'IVXLCDM'


def invert_dict(dictionary):
    return {v: k for k, v in dictionary.items()}


def _validate_arabic(arabic_number):
    return 0 <= int(arabic_number) < 4000


def _validate_roman(roman_number):
    one_type_symbols_allowed = 4
    one_type_symbols_in_row_allowed = 3
    symbols_presented = {}
    valid_symbols = True
    previous_symbol = None
    for sym in roman_number:
        if sym not in CONVERT_DICT.values():
            valid_symbols = False
            break
        if sym not in symbols_presented.keys():
            symbols_presented.update({sym: {'in_row': 1, 'general': 1}})
        else:
            if sym == previous_symbol:
                symbols_presented[sym]['in_row'] += 1
            symbols_presented[sym]['general'] += 1

    return len(list(filter(lambda s: symbols_presented[s]['general'] > one_type_symbols_allowed,
                           symbols_presented))) == 0 and \
           len(list(filter(lambda s: symbols_presented[s]['in_row'] > one_type_symbols_in_row_allowed,
                           symbols_presented))) == 0 and valid_symbols


def _convert_to_roman(arabic_number):
    multiplier = 1
    roman_number = ''
    for d in arabic_number[::-1]:
        if int(d) != 0:
            roman_number += CONVERT_DICT[int(d) * multiplier][::-1]
        multiplier *= 10
    return roman_number[::-1]


def _convert_to_arabic(roman_number):
    arabic_number = 0
    convert_dict = invert_dict(CONVERT_DICT)

    next_symbol = None
    current_symbol_position = 0
    for s in roman_number:
        if s not in SEQUENCE_RULE:
            raise ValueError

        if current_symbol_position < len(roman_number) - 1:
            next_symbol = roman_number[current_symbol_position + 1]

        if next_symbol and SEQUENCE_RULE.find(s) < SEQUENCE_RULE.find(next_symbol):
            arabic_number -= convert_dict[s]
        else:
            arabic_number += convert_dict[s]
        current_symbol_position += 1

    return arabic_number


def convert(number_data):
    handler = number_data['handler']
    return handler(number_data['number'])


def fetch_number_data(user_input):
    for i in user_input:
        if not str(i).isdigit():
            break
    else:
        return {'validator': _validate_arabic, 'handler': _convert_to_roman, 'number': user_input}

    for i in user_input:
        if i not in SEQUENCE_RULE:
            break
    else:
        return {'validator': _validate_roman, 'handler': _convert_to_arabic, 'number': user_input}

    raise ValueError


def main():
    user_input = input("Enter number: ")
    try:
        number_data = fetch_number_data(user_input)
        validator = number_data['validator']
        if not validator(number_data['number']):
            print("Number validation exception")
            raise ValueError
        print(convert(number_data))
    except ValueError:
        print("Incorrect input!")


if __name__ == '__main__':
    main()
