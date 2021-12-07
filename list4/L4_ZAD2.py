import time
import matplotlib.pyplot as plt
import numpy as np
from L4_ZAD1 import QueueBaB, QueueBaE

def time_measure(n: int):
    """
    Funkcja mierzy czas dodawania n elementów do kolejek QueueBab i QueueBaE oraz czas usuwania n elementów z kolejek; liczy
    średnią ilość czasu z dodawania i usuwania elementów z kolejek.
    
    param n: liczba elementów do dodania na listy
    return: zwraca krotkę z czasem: dodawania do kolejki BaB, dodawania do kolejki BaE, usuwania z BaB, usuwania z BaE, średnia
    czasów dla BaB, średnia czasów dla BaE
    """
    BaB=QueueBaB()
    BaE=QueueBaE()
    
    
    startB1=time.time()
    for i in range(n):
        BaB.enqueue(i)
    endB1= time.time()
        
    startE1=time.time()
    for i in range(n):
        BaE.enqueue(i)
    endE1=time.time()
    
    startB2=time.time()
    for _ in range(n):
        BaB.dequeue()
    endB2= time.time()
    
    startE2=time.time()
    for _ in range(n):
        BaE.dequeue()
    endE2=time.time()
    
    #średnia czasów z dodawania i usuwania z BaB i BaE
    sr_bab=(endB1-startB1+endE1-startE1)/2
    sr_bae=(endB2-startB2+endE2-startE2)/2
    
    return endB1-startB1, endB2-startB2,endE1-startE1,endE2-startE2, sr_bab,sr_bae


def compare_enqueue(n: int):
    """
    Funkcja rysuje wykresy czasu trwania dodawania n elementów do list QueueBaB i QueueBaE.
    
    param n: ilość elementów dodawanych do list
    """
    
    xb=np.linspace(0,n)
    timeb=np.linspace(0,time_measure(n)[0])
    xe=np.linspace(0,n)
    timee=np.linspace(0,time_measure(n)[1])
    

    plt.plot(xb,timeb, 'C4.',label='QueueBaB')
    plt.plot(xe,timee, 'C5.', label='QueueBaE')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Enqueue")
    
    plt.legend()
    plt.grid()
    plt.show()


def compare_dequeue(n: int):
    """
    Funkcja rysuje wykresy czasu trwania usuwania n elementów do list QueueBaB i QueueBaE.
    
    param n: ilość elementów usuwanych z list
    """
    
    xb=np.linspace(0,n)
    timeb=np.linspace(0,np.abs(time_measure(n)[2]))
    xe=np.linspace(0,n)
    timee=np.linspace(0,np.abs(time_measure(n)[3]))

    plt.plot(xb,timeb, 'C4.',label='QueueBaB')
    plt.plot(xe,timee, 'C5.', label='QueueBaE')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Dequeue")
    
    plt.legend()
    plt.grid()
    plt.show()

def compare_mean(n: int):
    """
    Funkcja rysuje wykresy średniej ilości czasu potrzbnej do dodania i usunięcia n elementów z list QueueBaB i QueueBaE.
    
    param n: ilość dodawanych i usuwanych elementów
    """
    
    xb=np.linspace(0,n)
    timeb=np.linspace(0,np.abs(time_measure(n)[4]))
    xe=np.linspace(0,n)
    timee=np.linspace(0,np.abs(time_measure(n)[5]))

    plt.plot(xb,timeb, 'C4.',label='QueueBaB')
    plt.plot(xe,timee, 'C5.', label='QueueBaE')
    plt.xlabel('Number of elements')
    plt.ylabel('Time')
    plt.title("Mean of enqueue and dequeue")
    
    plt.legend()
    plt.grid()
    plt.show()

#eksepryment na str
def open_txt(filename: str):
    """
    Funkcja otwiera i odczytuje plik .txt
    
    param filename: nazwa pliku txt
    return: listę wyrazów i znaków zawartych w pliku filename
    """
    f=open(filename,"r", encoding="utf-8")
    file=f.read()
    file=file.split()
    return file


def measure_time_str(filename: str):
    """
    Funkcja mierzy czas dodawania n elementów typu str do kolejek QueueBab i QueueBaE oraz czas usuwania n elementów z kolejek; liczy
    średnią ilość czasu z dodawania i usuwania elementów z kolejek.
    
    param n: liczba elementów do dodania i usunięcia z list
    return: zwraca krotkę z czasem: dodawania do kolejki BaB, dodawania do kolejki BaE, usuwania z BaB, usuwania z BaE, średnia
    czasów dla BaB, średnia czasów dla BaE
    """
    list_of_str=open_txt(filename)
    list_of_str=list_of_str*140 #aby rząd badanych elementów był taki sam jak rząd na liczbach
    BaB=QueueBaB()
    BaE=QueueBaE()
    
    startB1=time.time()
    for i in range(0,len(list_of_str)):
        BaB.enqueue(list_of_str[i])
    endB1=time.time()
    
    startE1=time.time()
    for i in range(0,len(list_of_str)):
        BaE.enqueue(list_of_str[i])
    endE1=time.time()
    
    startB2=time.time()
    for _ in range(0,len(list_of_str)):
        BaB.dequeue()
    endB2= time.time()
    
    startE2=time.time()
    for _ in range(0,len(list_of_str)):
        BaE.dequeue()
    endE2=time.time()
    
    #średnia czasów z dodawania i usuwania z BaB i BaE
    sr_bab=(endB1-startB1+endE1-startE1)/2
    sr_bae=(endB2-startB2+endE2-startE2)/2
    
    return endB1-startB1, endB2-startB2,endE1-startE1,endE2-startE2, sr_bab, sr_bae


    def compare_enqueue_str(filename: str):
    """
    Funkcja rysuje wykresy czasu trwania dodawania n elementów typu str do list QueueBaB i QueueBaE.
    
    param n: ilość elementów dodawanych do list
    """
    file_txt=open_txt(filename)
    
    xb=np.linspace(0,len(file_txt))
    timeb=np.linspace(0,measure_time_str(filename)[0])
    
    xe=np.linspace(0,len(file_txt))
    timee=np.linspace(0,measure_time_str(filename)[1])
    
    plt.plot(xb,timeb, 'C4.',label='QueueBaB')
    plt.plot(xe,timee, 'C5.', label='QueueBaE')
    plt.xlabel('Number of words')
    plt.ylabel('Time')
    plt.title("Enqueue")
    
    plt.legend()
    plt.grid()
    plt.show()
    
def compare_dequeue_str(filename: str):
    """
    Funkcja rysuje wykresy czasu trwania usuwania n elementów typu str do list QueueBaB i QueueBaE.
    
    param n: ilość elementów usuwanych z list
    """
    file_txt=open_txt(filename)
    
    xb=np.linspace(0,len(file_txt))
    timeb=np.linspace(0,measure_time_str(filename)[2])
    
    xe=np.linspace(0,len(file_txt))
    timee=np.linspace(0,measure_time_str(filename)[3])
    
    plt.plot(xb,timeb, 'C4.',label='QueueBaB')
    plt.plot(xe,timee, 'C5.', label='QueueBaE')
    plt.xlabel('Number of words')
    plt.ylabel('Time')
    plt.title("Dequeue")
    

    plt.legend()
    plt.grid()
    plt.show()
    