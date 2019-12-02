#!/usr/bin/env python
import unittest
from unittest.mock import Mock

from lab_9_4 import fetch_number_data, _validate_arabic, _convert_to_roman, _validate_roman, _convert_to_arabic, \
    invert_dict, convert


class NumbersConverterTest(unittest.TestCase):
    def test_fetch_number_data_arabic(self):
        number_data = str(123456)
        result = fetch_number_data(number_data)
        self.assertEqual(number_data, result['number'])
        self.assertEqual(_validate_arabic, result['validator'])
        self.assertEqual(_convert_to_roman, result['handler'])

    def test_fetch_number_data_roman(self):
        number_data = str('MXXVI')
        result = fetch_number_data(number_data)
        self.assertEqual(number_data, result['number'])
        self.assertEqual(_validate_roman, result['validator'])
        self.assertEqual(_convert_to_arabic, result['handler'])

    def test_fetch_number_data_incorrect_data(self):
        incorrect_number_data = str('4MX2X3VI')
        with self.assertRaises(ValueError):
            fetch_number_data(incorrect_number_data)

    def test_convert_to_arabic(self):
        arabic_number_1 = 1999
        arabic_number_2 = 3999
        arabic_number_3 = 123
        roman_number_1 = 'MCMXCIX'
        roman_number_2 = 'MMMCMXCIX'
        roman_number_3 = 'CXXIII'
        self.assertEqual(arabic_number_1, _convert_to_arabic(roman_number_1))
        self.assertEqual(arabic_number_2, _convert_to_arabic(roman_number_2))
        self.assertEqual(arabic_number_3, _convert_to_arabic(roman_number_3))

    def test_convert_to_roman(self):
        arabic_number_1 = '1999'
        arabic_number_2 = '3999'
        arabic_number_3 = '123'
        roman_number_1 = 'MCMXCIX'
        roman_number_2 = 'MMMCMXCIX'
        roman_number_3 = 'CXXIII'
        self.assertEqual(roman_number_1, _convert_to_roman(arabic_number_1))
        self.assertEqual(roman_number_2, _convert_to_roman(arabic_number_2))
        self.assertEqual(roman_number_3, _convert_to_roman(arabic_number_3))

    def test_validate_roman_correct_data(self):
        valid_roman_1 = 'MMMCMXCIX'
        valid_roman_2 = 'DLVI'
        valid_roman_3 = 'MCCCLVI'
        self.assertTrue(_validate_roman(valid_roman_1))
        self.assertTrue(_validate_roman(valid_roman_2))
        self.assertTrue(_validate_roman(valid_roman_1))

    def test_validate_roman_incorrect_data(self):
        incorrect_roman_1 = 'CMCMCCCCCCMCMXCIX'
        incorrect_roman_2 = 'LDDDDSLD'
        incorrect_roman_3 = 'CMMO'
        self.assertFalse(_validate_roman(incorrect_roman_1))
        self.assertFalse(_validate_roman(incorrect_roman_2))
        self.assertFalse(_validate_roman(incorrect_roman_3))

    def test_validate_arabic_correct_data(self):
        valid_arabic_1 = 3999
        valid_arabic_2 = 5
        valid_arabic_3 = 1998
        self.assertTrue(_validate_arabic(valid_arabic_1))
        self.assertTrue(_validate_arabic(valid_arabic_2))
        self.assertTrue(_validate_arabic(valid_arabic_3))

    def test_validate_arabic_incorrect_data(self):
        incorrect_arabic_1 = 4000
        incorrect_arabic_2 = -1
        self.assertFalse(_validate_arabic(incorrect_arabic_1))
        self.assertFalse(_validate_arabic(incorrect_arabic_2))

    def test_invert_dict(self):
        dict_ = {'key_1': 'val_1', 'key_2': 'val_2', 'key_3': 'val_3'}
        inverted_dict = {'val_1': 'key_1', 'val_2': 'key_2', 'val_3': 'key_3'}
        self.assertEqual(inverted_dict, invert_dict(dict_))

    def test_convert(self):
        handler = Mock()
        number = 123
        number_data = {'handler': handler, 'number': 123}
        convert(number_data)
        handler.assert_called_once_with(number)
