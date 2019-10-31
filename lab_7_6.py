#!/usr/bin/env python

ASTERISK_LINE_LENGTH_ADDER = 4


def pretty_print(line):
    asterisk_line_length = len(line) + ASTERISK_LINE_LENGTH_ADDER
    print('*' * asterisk_line_length)
    print(f'* {line} *')
    print('*' * asterisk_line_length)


if __name__ == '__main__':
    line = input('Enter line: ')
    pretty_print(line)
