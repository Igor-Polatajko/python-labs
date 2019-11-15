#!/usr/bin/env python
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return sum(self._get_sides())

    def get_area(self):
        half_perimeter = self.get_perimeter() / 2
        sides = self._get_sides()
        return sqrt(half_perimeter * (half_perimeter - sides[0]) * (half_perimeter - sides[1])
                    * (half_perimeter - sides[2]))

    def can_exist(self):
        sides = self._get_sides()
        return sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]

    def _get_sides(self):
        return [self.a.distance_to(self.b), self.b.distance_to(self.c), self.c.distance_to(self.a)]


if __name__ == '__main__':
    a_point = Point(0, 1)
    b_point = Point(1, 1)
    c_point = Point(1, 0)

    triangle = Triangle(a_point, b_point, c_point)

    print(triangle.can_exist())
    print(triangle.get_perimeter())
    print(triangle.get_area())
