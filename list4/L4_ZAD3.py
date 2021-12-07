from math import floor
from L4_ZAD1 import QueueBaB
from L4_ZAD6 import StackUsingUL
from random import randint

"""
Wyobraźmy sobie, że pewien hotel oferuje dla swoich gości transport z lotniska. Celem symulacji jest odpowiedź na 
pytanie ile autobusów powinno zostać podstawionych w danych odstępach czasu, aby przetransportować ludzi z lotniska 
do hotelu. Wiemy ile osób pojawia się na przystanku w ciągu minuty, jak dużo osób jest w stanie pomieścić nasz autobus
oraz jaka jest minimalna ilość osób, aby autobus został podstawiony.

Założenia:
- autobusy nie zatrzymują się na żadnych przystankach, na trasie nikt się nie dosiada
- autobusy kursują na tej samej trasie
- minimalnie musi uzbierać się 1/3 pojemności autobusu, aby zabrać czekające osoby do hotelu
- osoby które nie zmieściły się do autobusów na daną godzinę muszą poczekać w kolejce na kolejny kurs
- liczba autobusów kursująca w ustalonym okresie czasu jest zapisywana i przechowywana na stosie 
- w ciągu każdej minuty w ciągu doby może się pojawić osoba na przystanku
"""


class Bus():
    def __init__(self, capacity=54, interval=1):
        """
        @param capacity: max amount of passengers
        @param interval: number of 30-minutes periods
        """
        self.capacity = capacity
        self.minimum = capacity/3
        self.interval = interval


def simulation(capacity, interval=1, max_per_minute=5):
    """
    Performs a simulation how much buses is needed to transport a group of people.
    Contains list of people appearing at the bus stop per every minute.
    """
    bus = Bus()
    bus.capacity = capacity
    bus.interval = interval

    list_of_people = [randint(0, max_per_minute) for _ in range(1440)]

    waiting = QueueBaB()
    bus_plan = StackUsingUL()

    periods = [list_of_people[i:30*interval+i] for i in range(0, len(list_of_people), 30*interval)]

    for n in periods:
        group = sum(n)
        if not waiting.is_empty():
            tmp = waiting.dequeue()
        else:
            tmp = 0

        amount_of_buses = floor((group + tmp)/capacity)
        others = group % capacity
        if others >= bus.minimum:
            amount_of_buses += 1
        else:
            waiting.enqueue(others)

        bus_plan.push(amount_of_buses)

    return bus_plan


print(simulation(54, 4))
print(simulation(20, 1, 2))

