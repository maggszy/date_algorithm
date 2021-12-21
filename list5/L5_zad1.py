import numpy as np
from scipy import linalg
from scipy import stats
import time, random
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.optimize import curve_fit

#not good
def cramer_matrix(n):
    a = np.array([[random.randint(-500, 500) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-500, 500) for _ in range(n)])
    if np.linalg.det(a) != 0:
        return linalg.solve(a, b)

def cramer_matrix2(n):
    a = np.array(np.random.randint(0, 1000, size=(n, n)))
    b = np.array(np.random.randint(0, 1000, n))
    #x = linalg.solve(a, b)
    return linalg.solve(a, b)


def time_check(n):
    t0 = time.time()
    cramer_matrix2(n)
    t1 = time.time()

    return t1 - t0




# plt.plot(log_data(100)[0], log_data(100)[1])


def plotting2(num,step):
    x=[i for i in range(0,num,step)]
    times=[time_check(i) for i in x]

    slope = stats.linregress(x,times)[0]
    print("Slope", slope)


    plt.loglog(x, times, '.')
    # plt.plot(x, times, '.')
    # plt.plot(x)
    plt.xlabel("Wielkość macierzy") 
    plt.ylabel("Czas wykonania")
    plt.title("Złożoność obliczeniowa ")
    plt.grid()
    plt.show()

    



def checking(num, step):
    #x=[i for i in range(0,num,step)]
    #times=[time_check(i) for i in x]

    x = np.arange(0, num)
    plotting2(num, step)
    #plotting2(num, step)
    plt.show()

    #x= list(range(0,num,4))
    #times=[]
    #for i in x:
     #   times.append(time_check(i))

    #plotting2(x, times)

if __name__ == "__main__":


    #X, Y = log_data(1000)
    #plt.plot(X, Y)
    #plt.show()
    plotting2(500, 5)

    # x=[i for i in range(1, 1000, 15)]
    # times=[time_check(i) for i in x]

    # slope = stats.linregress(X, Y)[0]
    # print("Slope", slope)

    # approx_matrix = [slope*u for u in x]
    # plt.plot(x, times, '.')
    # plt.plot(approx_matrix, times)

    # plt.xlabel("Wielkość macierzy") 
    # plt.ylabel("Czas wykonania")
    # plt.title("Złożoność obliczeniowa ")
    # plt.grid()
    # plt.show()