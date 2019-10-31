#!/usr/bin/env python

VOWELS = ('a', 'o', 'u', 'i', 'e', 'y')


def calc_vowels_count(text):
    vowels_count = 0
    for symbol in text:
        if symbol.lower() in VOWELS:
            vowels_count += 1
    return vowels_count


if __name__ == '__main__':
    text = input("Enter the text: ")
    print(f"Vowels count: {calc_vowels_count(text)}")
