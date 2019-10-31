#!/usr/bin/env python
import csv
from random import shuffle

BATCH_SIZE = 64


def generator():
    with open('resources/titanic/train.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        batch = []
        count = 0
        for row in csv_reader:
            batch.append(row)
            count += 1
            if count >= BATCH_SIZE:
                shuffle(batch)
                yield batch
                count = 0
                batch = []


if __name__ == '__main__':
    gen_obj = generator()
    for data in gen_obj:
        print(data)
