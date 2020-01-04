#!/usr/bin/env python
from math import floor


class CurrencyNumberToWrittenFormTransformService:
    __NUMBERS = {
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

    def transform(self, amount_str):
        try:
            amount_int = float(amount_str)
        except ValueError:
            raise ValueError("Неправильний ввід")
        try:
            if amount_int > 999999.99:
                raise ValueError("Сума перевищує максимальну")

            if amount_int < 0:
                raise ValueError("Сума не може бути меншою за нуль")

            parts = self.__get_integer_parts(amount_str)
        except AssertionError:
            raise ValueError("Некоректий ввід!")
        else:
            return self.__to_written_form(parts)

    def __resolve_pronunciation(self, number):
        def _decide_by_number(n):
            if n == 1:
                return {'uah': 'гривня', 'coin': 'копійка', 'thousand': 'тисяча'}
            if n in (2, 3, 4):
                return {'uah': 'гривні', 'coin': 'копійки', 'thousand': 'тисячі'}
            return {'uah': 'гривень', 'coin': 'копійок', 'thousand': 'тисяч'}

        if number in (1, 2, 3, 4):
            return _decide_by_number(number)
        if number in self.__NUMBERS.keys():
            return {'uah': 'гривень', 'coin': 'копійок', 'thousand': 'тисяч'}

        last = int(str(number)[-1])
        if len(str(number)) > 1:
            before_last = int(str(number)[-2])
            if before_last == 1:
                last = int(str(last) + str(before_last))
        return _decide_by_number(last)

    def __get_integer_parts(self, number):
        parts = number.split('.')
        if len(parts) == 1:
            parts.append('0')
        parts[1] = parts[1][0:2]
        if len(parts[1]) == 1:
            parts[1] += '0'
        assert len(parts) == 2
        return dict(zip(['uah', 'coin'], list(map(lambda p: int(p), parts))))

    def __perform_advanced_resolving(self, number):
        result = ''
        multiplier = 1
        processing_of_last = True

        while number >= 1:
            if multiplier == 1000:
                multiplier = 1
                processing_of_last = True
                result += ' ' + self.__resolve_pronunciation(floor(number))['thousand']

            number_coef = 10
            multiplier_coef = 10

            if number % 10 != 0:
                if 10 < number % 100 < 20 and processing_of_last:
                    number_last_part = number % 100
                    number_coef = 100
                    multiplier_coef = 100
                else:
                    number_last_part = number % 10
                result += ' ' + self.__integer_part_convert(number_last_part * multiplier)
            multiplier *= multiplier_coef
            number = floor(number / number_coef)
            processing_of_last = False

        return ' '.join(reversed(result.split()))

    def __integer_part_convert(self, number):
        if number in self.__NUMBERS.keys():
            return self.__NUMBERS[number]
        return self.__perform_advanced_resolving(number)

    def __to_written_form(self, amount_parts):
        result = f"{self.__integer_part_convert(amount_parts['uah'])} \
    {self.__resolve_pronunciation(amount_parts['uah'])['uah']}"
        if amount_parts['coin'] != 0:
            result += f" {self.__integer_part_convert(amount_parts['coin'])} \
    {self.__resolve_pronunciation(amount_parts['coin'])['coin']}"
        return result
