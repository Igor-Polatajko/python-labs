#!/usr/bin/env python


def make_slice(input_string, shift):
    return input_string[shift:] + input_string[:shift]


def main():
    string = input("Enter the input string: ")
    while True:
        try:
            shift = int(input("Enter shift: "))
            if shift > len(string) / 2:
                print("Shift should not be bigger than half of the input string length")
                raise ValueError
        except ValueError:
            print("Incorrect input")
        else:
            string = make_slice(string, shift)
            print(f"Result string: {string}")


if __name__ == '__main__':
    main()
