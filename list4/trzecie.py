from math import floor
from L4_ZAD1 import QueueBaB
from L4_ZAD6 import StackUsingUL


class Bus():
    def __init__(self, capacity=54, interval=90):
        self.capacity = capacity
        self.minimum = capacity/3
        self.interval = interval


def simulation(capacity, interval):
    bus = Bus()
    bus.capacity = capacity
    bus.interval = interval
    list_of_people = [130, 200, 500, 100, 250, 180, 320, 120]
    # list_of_people = [54, 108, 162, 110, 54, 54, 108]

    waiting = QueueBaB()
    bus_plan = StackUsingUL()

    for i in list_of_people:
        if not waiting.is_empty():
            tmp = waiting.dequeue()
        else:
            tmp = 0

        amount_of_buses = floor((i + tmp)/capacity)
        others = i % capacity
        if others >= bus.minimum:
            amount_of_buses += 1
        else:
            waiting.enqueue(others)

        bus_plan.push(amount_of_buses)

    return bus_plan


print(simulation(54, 50))
