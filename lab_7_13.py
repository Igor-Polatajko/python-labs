#!/usr/bin/env python


def can_build_second_line_from_first(first_line, second_line):
    return len(list(filter(lambda s: s not in first_line, second_line))) == 0


if __name__ == '__main__':
    first_line = input("Enter first line: ")
    second_line = input("Enter second line: ")
    print(f"Can build second line from first: {can_build_second_line_from_first(first_line, second_line)}")
