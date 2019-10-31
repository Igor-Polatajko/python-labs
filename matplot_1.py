from matplotlib import pyplot as plt


if __name__ == '__main__':
    x = [1, 2, 3]
    y = [5, 7, 4]

    plt.plot(x, y, label="123")
    plt.xlabel('Plot Number')
    plt.ylabel('Plot Number')

    plt.title('Interesting Graph')
    plt.legend()
    plt.show()
