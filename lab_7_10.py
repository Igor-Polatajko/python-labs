#!/usr/bin/env python


def get_shortest_word_length(line):
    words = line.split()
    return min(map(lambda w: len(w), words))


if __name__ == '__main__':
    line = input("Enter line: ")
    print(f"Length of the shortest word: {get_shortest_word_length(line)}")
