class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

######################################
# Modelowanie ewakuacji uczesników wydarzenia autokarami.
# Założenia:
# Wszyscy jadą w to samo miejsce, autokar nie zatrzmuje się na przystankach na trasie, każdy uczestnik wydarzenia wraca autokarem.


######################################

class Bus:
    def __init__(self, arrival):
        self.newbus = arrival # jak często autobus podjeżdża na przystanek
        self.currentDrive = None
        self.timeRemaining = 0 # czas oczekiwania na kolejny kurs autobusu
        self.bus_capacity = 25

    def tick(self):
        if self.currentDrive != None:
            self.timeRemaining = self.timeRemaining - 1
        if self.timeRemaining <= 0:
            self.currentDrive = None

    def on_the_road(self):
        if self.currentDrive != None:
            return True
        else:
            return False

    def onboard(self):
        # return how much passengers is on board
        pass


class Passenger:
    def __init__(self, geton_time, rate):
        self.geton_time = geton_time
        self.rate = rate # w jakim tempie ludzie przychodza na przystanek
        self.person_id = 0

    def getStamp(self):
        return self.timestamp

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds):
    bus = Bus()
    group = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if Bus.on_the_road() < Bus.bus_capacity:
            passenger = Passenger(currentSecond)
            group.enqueue(passenger)

    if (not bus.on_the_road()) and (not group.isEmpty()):
        nexttask = group.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        bus.startNext(nexttask)

    bus.tick()

    # averageWait = sum(waitingtimes) / len(waitingtimes)
    # print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, group.size()))

