def approx(x,a,b,c):
    return a*x**2 + b*x + c


def approx_search(num,step):
    x=[i for i in range(0,num,step)]
    times=[]
    for i in x:
        times.append(i)

    popt, pcov = curve_fit(approx, x, times)
    a,b,c = popt
    return (a, b, c)


def cramer_matrix(n):
    a = np.array([[random.randint(-500, 500) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-500, 500) for _ in range(n)])
    if np.linalg.det(a) != 0:
        return linalg.solve(a, b)

def cramer_matrix2(n):
    a = np.array(np.random.randint(-100, 100, size=(n, n)))
    b = np.array(np.random.randint(-100, 100, n))
    #x = linalg.solve(a, b)
    return linalg.solve(a, b)


def time_check(n):
    t0 = time.time()
    cramer_matrix2(n)
    t1 = time.time()

    return t1 - t0

def log_data(n):
    x=[i for i in range(1,n+1, 15)]
    times=[time_check(i) for i in x]

    log_n = [np.log(i) for i in x]
    log_time = []
    for i in times:
        if i == 0:
            log_time.append(0)
        else:
            log_time.append(np.log(i))

    return log_n, log_time



# plt.plot(log_data(100)[0], log_data(100)[1])

def plotting(x, y):
    plt.plot(x, y, '.')
    #p = Polynomial.fit(x, y, 2)
    #plt.plot(*p.linspace())
    plt.xlabel("Wielkość macierzy") 
    plt.ylabel("Czas wykonania")
    plt.title("Złożoność obliczeniowa ")
    plt.grid()
    plt.show()


def plotting2(num,step):
    x=[i for i in range(0,num,step)]
    times=[time_check(i) for i in x]
    
    popt, pcov = curve_fit(approx, x, times)
    # plt.plot(x, approx(x, *popt))
    # a,b,c= approx_search(num, step)

    plt.plot(x, times, '.')
    # plt.plot(x, approx(x, a, b, c))
    # plt.plot(x, approx(x, *popt))
    plt.xlabel("Wielkość macierzy") 
    plt.ylabel("Czas wykonania")
    plt.title("Złożoność obliczeniowa ")
    plt.grid()
    plt.show()



def checking(num, step):
    #x=[i for i in range(0,num,step)]
    #times=[time_check(i) for i in x]

    a= approx_search(num, step)[0]
    b= approx_search(num, step)[1]
    c=approx_search(num, step)[2]
    #print(approx_search(num, step))
    x = np.arange(0, num)
    plotting2(num, step)
    plt.plot(x, approx(x, a, b, c))
    #plotting2(num, step)
    plt.show()

    #x= list(range(0,num,4))
    #times=[]
    #for i in x:
     #   times.append(time_check(i))

    #plotting2(x, times)

if __name__ == "__main__":
    #checking(500,3)
    #cramer_matrix(30)
    #time_check(30)
    # plotting2(500, 30)


    X, Y = log_data(1000)
    plt.plot(X, Y)
    plt.show()

    # x=[i for i in range(1, 1000, 15)]
    # times=[time_check(i) for i in x]

    slope = stats.linregress(X, Y)[0]
    print("Slope", slope)

    # approx_matrix = [slope*u for u in x]
    # plt.plot(x, times, '.')
    # plt.plot(approx_matrix, times)

    # plt.xlabel("Wielkość macierzy") 
    # plt.ylabel("Czas wykonania")
    # plt.title("Złożoność obliczeniowa ")
    # plt.grid()
    # plt.show()

    """n = [5, 10, 20, 34, 45, 50, 70, 85, 90, 100]
    times = []
    for i in n:
        times.append(time_check(i))

    plotting(n, times)"""



def log_data(n):
    x=[i for i in range(1,n+1, 15)]
    times=[time_check(i) for i in x]

    log_n = [np.log(i) for i in x]
    log_time = []
    for i in times:
        if i == 0:
            pass
            # log_time.append(0)
        else:
            log_time.append(np.log(i))

    return log_n, log_time