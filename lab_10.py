#!/usr/bin/env python
from math import floor

from PIL import Image


def read_img_from_file(file_path):
    return Image.open(file_path, 'r').copy()


def str_to_bin(string):
    return list(format(ord(c), '#010b')[2::] for c in string)


def calc_indent(x, y, word_len=160):
    return floor((x * y / word_len) ** (1 / 2))


def encode(img, string):
    pixels = img.load()
    binary = str_to_bin(string)
    indent = calc_indent(img.size[0], img.size[1])

    it = 0
    x_indent = 0
    y_indent = 0
    while it < len(binary):
        if x_indent >= img.size[0]:
            y_indent += indent
            x_indent = 0
            if y_indent >= img.size[0]:
                break

        p = pixels[x_indent, y_indent]
        pixels[x_indent, y_indent] = (p[0], p[1], int(binary[it], 2), 255)

        x_indent += indent
        it += 1
    pixels[x_indent, y_indent] = 0

    return img


def decode(img):
    result = ''
    pixels = img.load()
    indent = calc_indent(img.size[0], img.size[1])

    it = 0
    x_indent = 0
    y_indent = 0
    while True:
        if x_indent >= img.size[0]:
            y_indent += indent
            x_indent = 0
            if y_indent >= img.size[1]:
                break
        if pixels[x_indent, y_indent][2] == 0:
            break

        result += chr(pixels[x_indent, y_indent][2])

        x_indent += indent
        it += 1
    return result


def main():
    while True:
        print("""Hello! What would you like to do?
                 [1] - encode data
                 [2] - decode data
                 """)
        try:
            user_input = int(input("Your choice: "))
            if user_input not in (1, 2):
                raise ValueError
            break
        except ValueError:
            print("Incorrect input!\n")

    if user_input == 1:
        try:
            file_path = input("Provide path to file to encode data in: ")
            string_to_encode = input("Provide string to encode: ")
            output_image_path = input("Provide path to output file: ")

            img = read_img_from_file(file_path)
            img = encode(img, string_to_encode)
            img.save(output_image_path)
        except FileNotFoundError:
            print("File not found!")
    else:
        encoded_file_path = input("Provide path to encoded file: ")
        img_from_file = read_img_from_file(encoded_file_path)
        print("Encoded data:")
        print(decode(img_from_file))


if __name__ == '__main__':
    main()
