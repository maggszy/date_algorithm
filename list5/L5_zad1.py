import numpy as np
from scipy import linalg
from scipy import stats
import time, random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def cramer_matrix(n):
    a = np.array([[random.randint(-50, 50) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-50, 50) for _ in range(n)])
    return linalg.solve(a, b)


def time_check(n):
    t0 = time.time()
    cramer_matrix(n)
    t1 = time.time()

    return t1 - t0



def log_plot(min=500, max=8000, step=800):
    x = [i for i in range(min, max, step)]
    times = [time_check(i) for i in x]

    slope = stats.linregress(np.log(x), np.log(times))[0]

    plt.plot(x, times, '.', label='Dane')
    plt.loglog(x, times, label='Wsp kierunkowy = %4f' % slope)

    plt.xlabel("Wielkość macierzy")
    plt.ylabel("Czas wykonania operacji")
    plt.title("Wykres czasu w zależności od wielkości macierzy w skali logarytmicznej")
    plt.grid()
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    #log_plot(500, 6000, 200)
    log_plot()