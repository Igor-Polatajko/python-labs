#!/usr/bin/env python


def calc_alive(people_number):
    people_list = []
    [people_list.append(i) for i in range(1, people_number + 1)]
    temp = 0
    while len(people_list) > 1:
        current_circle_remove = []
        while temp < len(people_list):
            current_circle_remove.append(temp)
            temp += 2
        temp -= len(people_list)
        [people_list.pop(i) for i in reversed(current_circle_remove)]

    return people_list[0]


if __name__ == '__main__':
    try:
        people_number = int(input("Enter people number: "))
        if people_number < 1:
            raise ValueError
    except ValueError:
        print("Incorrect input")
    else:
        print(f"The last one: {calc_alive(people_number)}")
