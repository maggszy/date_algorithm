from L4_ZAD5 import UnorderedList
import time, matplotlib.pyplot as plt, numpy as np

mylist = UnorderedList()
pylist = []


def list_analysis(n):
    startml_1 = time.time()
    for i in range(n):
        mylist.add(i)
    endml_1 = time.time()

    startpy_1 = time.time()
    for i in range(n):
        pylist.insert(0, i)
    endpy_1 = time.time()

    startml_n = time.time()
    for _ in range(n):
        mylist.append(i)
    endml_n = time.time()

    startpy_n = time.time()
    for _ in range(n):
        pylist.append(i)
    endpy_n = time.time()

    return endml_1 - startml_1, endpy_1 - startpy_1, endml_n - startml_n, endpy_n - startpy_n


def add_first(n):  # number of elements

    xb = np.linspace(0, n)
    timeb = np.linspace(0, list_analysis(n)[0])
    xe = np.linspace(0, n)
    timee = np.linspace(0, list_analysis(n)[1])

    plt.plot(xb, timeb, 'C1.', label='UnorderedList')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Adding to the first position")

    plt.plot(xe, timee, 'C2.', label='Python list')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Adding to the first position")

    plt.legend()
    plt.grid()
    plt.show()


def add_last(n):  # number of elements

    xb = np.linspace(0, n)
    timeb = np.linspace(0, list_analysis(n)[2])
    xe = np.linspace(0, n)
    timee = np.linspace(0, list_analysis(n)[3])

    plt.plot(xb, timeb, 'C1.', label='UnorderedList')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Adding to the last position")

    plt.plot(xe, timee, 'C2.', label='Python list')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Adding to the last position")

    plt.legend()
    plt.grid()
    plt.show()


def pop_analysis(n):
    startml = time.time()
    for i in range(n):
        mylist.pop()
    endml = time.time()

    startpy = time.time()
    for i in range(n):
        pylist.pop()
    endpy = time.time()

    return endml - startml, endpy - startpy


def pop_method(n):  # number of elements

    xb = np.linspace(0, n)
    timeb = np.linspace(0, pop_analysis(n)[0])
    xe = np.linspace(0, n)
    timee = np.linspace(0, pop_analysis(n)[1])

    plt.plot(xb, timeb, 'C1.', label='UnorderedList')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Using pop method")

    plt.plot(xe, timee, 'C2.', label='Python list')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Using pop method")

    plt.legend()
    plt.grid()
    plt.show()
