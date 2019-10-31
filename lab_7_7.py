#!/usr/bin/env python


def to_camel(line):
    parts = line.split('_')
    return parts[0] + ''.join(list(map(lambda s: str(s).capitalize(), parts[1:])))


if __name__ == '__main__':
    line = input('Enter line: ')
    print(f"Result: {to_camel(line)}")
