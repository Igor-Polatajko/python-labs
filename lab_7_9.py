#!/usr/bin/env python
from math import floor


def is_lucky(ticket_number):
    first_part_sum = 0
    second_part_sum = 0
    for i in range(floor((len(ticket_number) / 2))):
        first_part_sum += int(ticket_number[i])
        second_part_sum += int(ticket_number[-i - 1])
    return first_part_sum == second_part_sum


if __name__ == '__main__':
    ticket_number = input("Enter ticket number: ")
    try:
        print(f"Ticket is lucky: {is_lucky(ticket_number)}")
    except ValueError:
        print("Incorrect input")
