#!/usr/bin/env python
import sys
import unittest
from io import StringIO
from unittest.mock import patch

from lab_9_2 import resolve_pronunciation, get_integer_parts, perform_advanced_resolving, integer_part_convert, \
    to_written_form, main


class CurrencyConverterTest(unittest.TestCase):
    def test_resolve_pronunciation_type_1(self):
        type_1 = {'uah': 'гривень', 'coin': 'копійок', 'thousand': 'тисяч'}
        self.assertEqual(type_1, resolve_pronunciation(35))
        self.assertEqual(type_1, resolve_pronunciation(125))
        self.assertEqual(type_1, resolve_pronunciation(1789))

    def test_resolve_pronunciation_type_2(self):
        type_2 = {'uah': 'гривні', 'coin': 'копійки', 'thousand': 'тисячі'}
        self.assertEqual(type_2, resolve_pronunciation(1854))
        self.assertEqual(type_2, resolve_pronunciation(283))
        self.assertEqual(type_2, resolve_pronunciation(122))

    def test_resolve_pronunciation_type_3(self):
        type_3 = {'uah': 'гривня', 'coin': 'копійка', 'thousand': 'тисяча'}
        self.assertEqual(type_3, resolve_pronunciation(1))
        self.assertEqual(type_3, resolve_pronunciation(261))
        self.assertEqual(type_3, resolve_pronunciation(21))

    def test_get_integer_parts(self):
        self.assertEqual({'uah': 12, 'coin': 34}, get_integer_parts('12.34'))
        self.assertEqual({'uah': 153, 'coin': 30}, get_integer_parts('153.3'))
        self.assertEqual({'uah': 218, 'coin': 55}, get_integer_parts('218.55465845'))
        self.assertEqual({'uah': 0, 'coin': 15}, get_integer_parts('0.15'))

    def test_perform_advanced_resolving(self):
        self.assertEqual('одна тисяча п\'ятсот вісімдесят шість', perform_advanced_resolving(1586))
        self.assertEqual('дві тисячі триста вісімдесят три', perform_advanced_resolving(2383))
        self.assertEqual('сто одинадцять тисяч сто одинадцять', perform_advanced_resolving(111111))

    def test_integer_part_convert(self):
        with patch('lab_9_2.perform_advanced_resolving', return_value='delegate to advanced resolving'):
            self.assertEqual('delegate to advanced resolving', integer_part_convert(111111))
            self.assertEqual('delegate to advanced resolving', integer_part_convert(112))
            self.assertEqual('нуль', integer_part_convert(0))
            self.assertEqual('сто', integer_part_convert(100))

    def test_to_written_form(self):
        self.assertEqual('одна тисяча двісті тридцять чотири гривні п\'ятдесят шість копійок',
                         to_written_form({'uah': 1234, 'coin': 56}))
        self.assertEqual('нуль гривень',
                         to_written_form({'uah': 0, 'coin': 0}))
        self.assertEqual('одинадцять тисяч вісімсот дев\'ятнадцять гривень тридцять шість копійок',
                         to_written_form({'uah': 11819, 'coin': 36}))
        self.assertEqual('дві гривні двадцять шість копійок',
                         to_written_form({'uah': 2, 'coin': 26}))

    def test_main_zero_value(self):
        output = self._with_mock_input(main, '0')
        self.assertEqual('Письмова форма запису: нуль гривень', output)

    def test_main_tricky_number(self):
        output = self._with_mock_input(main, '111111.1')
        self.assertEqual('Письмова форма запису: сто одинадцять тисяч сто одинадцять'
                         ' гривень десять копійок', output)

    def test_main_out_of_bounds(self):
        output = self._with_mock_input(main, '1000000')
        self.assertEqual('Сума перевищує максимальну\nНекоректий ввід!', output)

    def test_main_less_than_zero(self):
        output = self._with_mock_input(main, '-1')
        self.assertEqual('Сума не може бути меншою за нуль\nНекоректий ввід!', output)

    def test_main_incorrect_input_symbol(self):
        output = self._with_mock_input(main, 'abc123')
        self.assertEqual('Некоректий ввід!', output)

    def _with_mock_input(self, method, input_mock_value):
        out = StringIO()
        saved_stdout = sys.stdout
        sys.stdout = out
        with patch('builtins.input', return_value=input_mock_value):
            method()
        sys.stdout = saved_stdout
        return out.getvalue().strip()


if __name__ == '__main__':
    unittest.main()
