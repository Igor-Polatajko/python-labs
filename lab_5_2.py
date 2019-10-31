#!/usr/bin/env python


def is_input_valid(data):
    for key in data.keys():
        if data[key] <= 0:
            return False
    return True


def get_user_input():
    door_size = dict()
    box_size = dict()

    door_size["height"] = float(input("Enter the height of the door: "))
    door_size["width"] = float(input("Enter the width of the door: "))
    box_size["a"] = float(input("Enter the 'a' side length of the box: "))
    box_size["b"] = float(input("Enter the 'b' side length of the box: "))
    box_size["c"] = float(input("Enter the 'c' side length of the box: "))
    if not is_input_valid(door_size) or not is_input_valid(box_size):
        raise ValueError
    return door_size, box_size


def can_fit_box_through_door(door_size, box_size):
    for one_side in box_size.keys():
        for another_side in box_size.keys():
            if one_side is another_side:
                continue
            if box_size[one_side] < door_size["height"] and box_size[another_side] < door_size["width"] or \
                    box_size[one_side] < door_size["width"] and box_size[another_side] < door_size["height"]:
                return True
    return False


def main():
    try:
        door_size, box_size = get_user_input()
        print(("Yes, there is the way" if can_fit_box_through_door(door_size, box_size) else "There is no way"),
              "to fit the box through the door")
    except ValueError:
        print("Incorrect input")


if __name__ == '__main__':
    main()
