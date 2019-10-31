#!/usr/bin/env python
import re


def remove_redundant_spaces(line):
    return re.sub(r'\s+', ' ', line)


if __name__ == '__main__':
    line = input("Enter line: ")
    print(f"Line without redundant spaces: {remove_redundant_spaces(line)}")
