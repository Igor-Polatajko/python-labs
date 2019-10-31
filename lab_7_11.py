#!/usr/bin/env python


def sort_by_length(line):
    return ' '.join(sorted(line.split(), key=len))


if __name__ == '__main__':
    line = input("Enter line: ")
    print(f"Sorted line: {sort_by_length(line)}")
