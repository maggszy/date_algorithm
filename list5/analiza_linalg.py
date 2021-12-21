import numpy as np
from scipy import linalg
from scipy import stats
import time, random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def cramer_matrix(n):
    a = np.array([[random.randint(-50, 50) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-50, 50) for _ in range(n)])
    # if np.linalg.det(a) != 0:
    return linalg.solve(a, b)


def time_check(n):
    t0 = time.time()
    cramer_matrix(n)
    t1 = time.time()

    return t1 - t0


###### slope wychodzi dwa z hakiem ####
def log_plot(min=500, max=8000, step=800):
    x = [i for i in range(min, max, step)]
    times = [time_check(i) for i in x]

    slope = stats.linregress(np.log(x), np.log(times))[0]

    plt.plot(x, times, '.', label='Dane')
    plt.loglog(x, times, label='slope=%4f' % slope)

    plt.xlabel("Wielkość macierzy")
    plt.ylabel("Czas wykonania operacji")
    plt.title("Wykres czasu w zależności od wielkości macierzy w skali logarytmicznej")
    plt.grid()
    plt.legend(loc='upper left')
    plt.show()


def func(x, a, b, power):
    return a * x ** power + b


###### to chyba do usunięcia #####
def fit_plot(min=500, max=8000, step=800):
    x = [i for i in range(min, max, step)]
    times = [time_check(i) for i in x]

    plt.plot(x, times, '.', label='Dane')

    popt, pcov = curve_fit(func, x, times)
    plt.plot(x, func(x, *popt), label='fit:a=%4f, b=%4f, c=%4f' % tuple(popt))
    print(popt)

    plt.xlabel("Wielkość macierzy")
    plt.ylabel("Czas wykonania operacji")
    plt.title("Wykres czasu w zależności od wielkości macierzy")
    plt.grid()
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    log_plot(500, 6000, 200)
