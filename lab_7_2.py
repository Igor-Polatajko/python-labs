#!/usr/bin/env python
import re


def is_palindrome(string):
    string = re.sub(r'[?.!/;:\'"-(){}\[\]\s]', '', string).lower()
    return string == string[::-1]


def main():
    string = input("Enter string to test: ")
    print(f"Palindrome test result: {is_palindrome(string)}")


if __name__ == '__main__':
    main()
