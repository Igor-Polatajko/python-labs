#!/usr/bin/env python
import random
import string

RAND_SECTION_MIN_LENGTH = 2
RAND_SECTION_MAX_LENGTH = 5


def random_line_of(seq):
    return ''.join(random.choice(seq) for x in range(RAND_SECTION_MIN_LENGTH, RAND_SECTION_MAX_LENGTH))


def generate_password():
    uppercase_chars = random_line_of(string.ascii_uppercase)
    lowercase_chars = random_line_of(string.ascii_lowercase)
    spec_chars = random_line_of(string.punctuation)
    digits = random_line_of(string.digits)
    password_symbols = (list(uppercase_chars + lowercase_chars + spec_chars + digits))
    random.shuffle(password_symbols)
    return ''.join(password_symbols)


if __name__ == '__main__':
    print(f"Your password: {generate_password()}")
