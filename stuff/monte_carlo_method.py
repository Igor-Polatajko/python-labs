#!/usr/bin/env python
import math
import random

from matplotlib import pyplot as plt

CENTER_POINT = {'x': 0, 'y': 0}
LOWER_BOUND = -10
UPPER_BOUND = 10
TEST_DATA_SCOPES = [10, 50, 100, 500, 1000, 2000, 10000, 50000, 100000]


def generate_random_position():
    return {'x': random.uniform(LOWER_BOUND, UPPER_BOUND), 'y': random.uniform(LOWER_BOUND, UPPER_BOUND)}


def is_in_circle(point):
    return math.sqrt((point['x'] - CENTER_POINT['x']) ** 2 + (point['y'] - CENTER_POINT['y']) ** 2) <= UPPER_BOUND


def calc_pi(inner, total):
    return 4 * inner / total


def get_random_points(count):
    return [generate_random_position() for _ in range(0, count)]


def estimate_pi(points):
    return calc_pi(len(get_inner_points(points)), len(points))


def get_inner_points(points):
    return list(filter(lambda p: is_in_circle(p), points))


def get_outer_points(points):
    return list(filter(lambda p: not is_in_circle(p), points))


def calc_deviation(estimation_results):
    return list(map(lambda r: abs(math.pi - r), estimation_results))


def draw_visual_repr(points):
    fig = plt.figure(2, figsize=(8, 8))
    ax1 = fig.add_subplot(111)
    inner_points = get_inner_points(points)
    outer_points = get_outer_points(points)
    plt.title(f"Points count: {len(points)}")
    ax1.scatter(list(map(lambda p: p['x'], inner_points)), list(map(lambda p: p['y'], inner_points)), c='r', s=1)
    ax1.scatter(list(map(lambda p: p['x'], outer_points)), list(map(lambda p: p['y'], outer_points)), c='b', s=1)
    plt.show()


def draw_pi_plot(estimation_results):
    plt.figure(1)
    plt.title("Deviation")
    x_list = list(range(0, len(estimation_results)))
    plt.plot(x_list, calc_deviation(estimation_results))
    plt.xticks(ticks=x_list, labels=TEST_DATA_SCOPES)
    plt.show()


def main():
    estimation_results = []
    for total in TEST_DATA_SCOPES:
        points = get_random_points(total)
        estimation_results.append(estimate_pi(points))
        draw_visual_repr(points)
    print(f"Estimation results: {estimation_results}")
    draw_pi_plot(estimation_results)


if __name__ == '__main__':
    main()
