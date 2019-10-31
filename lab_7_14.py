#!/usr/bin/env python
import re


def is_email_valid(email):
    return re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,5})+$", email) is not None


if __name__ == '__main__':
    email = input("Enter email: ")
    print(f"Is email valid: {is_email_valid(email)}")
