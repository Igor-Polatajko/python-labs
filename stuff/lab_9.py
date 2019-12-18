import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def draw_hist(data):
    plt.hist(data, density=True, histtype='stepfilled', alpha=0.2)
    plt.show()


def main():
    data = stats.norm.rvs(loc=10, scale=5, size=100000)
    sample = np.random.choice(data, 1000)
    mean = sample.mean()
    z_value = stats.norm.ppf(q=0.95)
    right_limit = mean + z_value
    left_limit = mean - z_value

    print(f"Mean: {mean}")
    print(f"z-value: {z_value}")
    print(f"Alpha and Beta: [ {left_limit}, {right_limit}]")
    draw_hist(data)


if __name__ == '__main__':
    main()
