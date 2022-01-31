import sys


class Queue:  # using in bfs
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


class Stack:  # using in topological sort
    def __init__(self):
        self.list_of_items = []

    def push(self, item):
        self.list_of_items.append(item)

    def peek(self):
        return self.list_of_items[len(self.list_of_items) - 1]

    def pop(self):
        return self.list_of_items.pop()

    def is_empty(self):
        return self.list_of_items == []

    def size(self):
        return len(self.list_of_items)

    def __str__(self):
        return str(self.list_of_items)


class BinHeap:  # using in Priority Queue
    def __init__(self):
        self.heapList = [{'key': 'head', 'weight': 'None'}]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i]['weight'] < self.heapList[i // 2]['weight']:
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


class PriorityQueue:  # using in dijkstra

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


class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'       #new: color of node
        self.dist = sys.maxsize    #new: distance from beginning (will be used later)
        self.pred = None           #new: predecessor
        self.disc = 0              #new: discovery time
        self.fin = 0               #new: end-of-processing time

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    # methods added to BasicGraph class from task 1
    def bfs(g, start):
        start.setDistance(0)                            #distance 0 indicates it is a start node
        start.setPred(None)                             #no predecessor at start
        vertQueue = Queue()
        vertQueue.enqueue(start)                        #add start to processing queue
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()           #pop next node to process -> current node
            for nbr in currentVert.getConnections():    #check all neighbors of the current node
                if (nbr.getColor() == 'white'):         #if the neighbor is white
                    nbr.setColor('gray')                             #change its color to grey
                    nbr.setDistance(currentVert.getDistance() + 1)   #set its distance
                    nbr.setPred(currentVert)                         #current node is its predecessor
                    vertQueue.enqueue(nbr)                           #add it to the queue
            currentVert.setColor('black')               #change current node to black after visiting all of its neigh.

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def topological_sort(self):
        pass


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
