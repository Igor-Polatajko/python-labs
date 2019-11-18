#!/usr/bin/env python
from math import sin, cos, radians


class FileIOHandler:
    @staticmethod
    def read_from_file(file_path):
        with open(file_path) as file:
            file_content = [line.strip() for line in file.readlines()]
        assert len(file_content) > 1
        angle = int(file_content[0].split()[1])
        data = [StarFactory.generate_star(line) for line in file_content[1::]]

        return angle, data

    @staticmethod
    def save_to_file(file_path, data_to_save):
        with open(f"{file_path}/output.txt", "w+") as file:
            for line in data_to_save:
                file.write(str(line) + " ")


class StarFactory:
    @staticmethod
    def generate_star(line):
        splitted = line.split()
        return Star(splitted[0], int(splitted[1]), int(splitted[2]))


class Star:
    def __init__(self, name, x_coord, y_coord):
        assert abs(x_coord) <= 1000 and abs(y_coord) <= 1000
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord

    def rotate(self, angle):
        assert 0 <= angle <= 360
        angle_rad = radians(angle)
        self.x_coord = round(self.x_coord * cos(angle_rad) - self.y_coord * sin(angle_rad))
        self.y_coord = round(self.x_coord * sin(angle_rad) + self.y_coord * cos(angle_rad))

    def __repr__(self):
        return self.name


def main():
    try:
        angle, data = FileIOHandler.read_from_file("./resources/input.txt")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("Error while reading the file")
    else:
        for star in data:
            star.rotate(angle)
        data.sort(key=lambda d: (d.y_coord, d.x_coord))
        print(data)
        FileIOHandler.save_to_file("./resources", data)


if __name__ == '__main__':
    main()
