#!/usr/bin/env python


OPEN_BRACKETS = ('<', '[', '(', '{')
CLOSE_BRACKETS = ('>', ']', ')', '}')
BRACKETS_PAIRS = dict(zip(CLOSE_BRACKETS, OPEN_BRACKETS))


def is_brackets_sequence_correct(line):
    brackets_stack = []
    for symbol in line:
        if symbol in OPEN_BRACKETS:
            brackets_stack.append(symbol)
        elif symbol in CLOSE_BRACKETS:
            if BRACKETS_PAIRS[symbol] != brackets_stack.pop():
                return False
    return len(brackets_stack) == 0


def main():
    line = input("Enter string to test: ")
    print(f"Brackets sequence test result: {is_brackets_sequence_correct(line)}")


if __name__ == '__main__':
    main()
