#!/usr/bin/env python


def next_symbol(symbol):
    if ord(symbol) == ord('z'):
        return 'a'
    if ord(symbol) == ord('Z'):
        return 'A'
    return chr(ord(symbol) + 1)


def encrypt(raw):
    encrypted = ''
    for symbol in raw:
        encrypted += next_symbol(symbol)
    return encrypted


if __name__ == '__main__':
    raw = input("Enter raw text: ")
    print(f"Encrypted: {encrypt(raw)}")
