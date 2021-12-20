import numpy as np
from scipy import linalg
import time, random
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial


def cramer_matrix(n):
    a = np.array([[random.randint(-50, 50) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-50, 50) for _ in range(n)])
    if np.linalg.det(a) != 0:
        return linalg.solve(a, b)


def time_check(n):
    t0 = time.time()
    cramer_matrix(n)
    t1 = time.time()

    return t1 - t0


def plotting(x, y):
    plt.plot(x, y, '.')
    p = Polynomial.fit(x, times, 2)
    plt.plot(*p.linspace())
    plt.xlabel("Wielkość macierzy")
    plt.ylabel("Czas wykonania")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    n = [5, 10, 20, 34, 45, 50, 70, 85, 90, 100]
    times = []
    for i in n:
        times.append(time_check(i))

    plotting(n, times)
