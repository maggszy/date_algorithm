class BinHeap:
    def __init__(self):
        self.heapList = [{'key': 'head', 'weight': 'None'}]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, key, weight):
        elem = {'key': key, 'weight': weight}
        self.heapList.append(elem)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i]['weight'] > self.heapList[mc]['weight']:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2]['weight'] < self.heapList[i * 2 + 1]['weight']:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        new = BinHeap().heapList
        self.heapList = new + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


###############################################
class PriorityQueue:

    def __init__(self):
        self.bh = BinHeap()

    def enqueue(self, key, weight):
        self.bh.insert(key, weight)

    def dequeue(self):
        return self.bh.delMin()

    def isEmpty(self):
        return self.bh.currentSize == 0

    def decreaseKey(self, key, weight):
        i = 1
        while i < (self.currentSize() + 1):
            if self.bh.heapList[i]['key'] == key:
                self.bh.heapList[i]['weight'] = weight
                self.bh.percUp(i)
            else:
                i = i + 1

    def loadPriorityQueue(self, list):
        self.bh.buildHeap(list)

    def currentSize(self):
        return self.bh.currentSize


def KeyWeightList(self):
    l = []
    for i in self.getVertices():
        dict= {}
        dict['key'] = i
        dict['weight'] = self.getVertex(i).getDistance()
        l.append(dict)

        return l


def dijkstra(Graph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.loadPriorityQueue([(v.getDistance(), v) for v in Graph])
    while not pq.isEmpty():
        key = pq.dequeue()['key']
        currentVert = Graph.getVertex(key)
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)

