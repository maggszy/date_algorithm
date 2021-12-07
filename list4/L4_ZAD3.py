from math import floor
from L4_ZAD1 import QueueBaB
from L4_ZAD6 import StackUsingUL
from random import randint


class Bus():
    def __init__(self, capacity=54, interval=90):
        self.capacity = capacity
        self.minimum = capacity/3
        self.interval = interval


def simulation(capacity, interval=1):
    bus = Bus()
    bus.capacity = capacity
    bus.interval = interval
    # list_of_people = [130, 200, 500, 100, 250, 180, 320, 120]
    list_of_people = [randint(0, 10) for i in range(1440)]
    # list_of_people = [54, 108, 162, 110, 54, 54, 108]

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


print(simulation(54, 2))


