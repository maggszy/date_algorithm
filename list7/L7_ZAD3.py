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


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'       #new: color of node
        self.dist = sys.maxsize    #new: distance from beginning (will be used later)
        self.pred = None           #new: predecessor
        self.disc = 0              #new: discovery time
        self.fin = 0               #new: end-of-processing time
        self.visited = False
        self.previous = None

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

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self, f ,t , cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def getEdges(self):
        edges = []
        for v in self:
            for w in v.get_connections():
                edges.append((v.get_id(), w.get_id()))
        return edges

    def getWeight(self, v1, v2):
        if self.vertList[v2] in self.vertList[v1].connectedTo:
            return self.vertList[v1].connectedTo[self.vertList[v2]]

    # methods added to BasicGraph class from task 1
    # rozszerzenie bfs aby by??a mo??liwo???? znale???? ??cie??k?? do wybranego lub ka??dego w??z??a
    def bfs(self, start, end=None):
        start = self.getVertex(start)
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


        if end != None:
            start = self.getVertex(start)
            end = self.getVertex(end)

            start.setDistance(0)
            start.setPred(None)
            listOfDistances = []
            for element in self.getVertices():
                listOfDistances.append([self.getVertex(element).dist, self.getVertex(element).id])

                while listOfDistances != []:
                    listOfDistances = sorted(listOfDistances, reverse=True)

                    currentVert = self.getVertex(listOfDistances.pop()[1])
                    if currentVert.dist == sys.maxsize:
                        break

                    for nbr in currentVert.getConnections():
                        alternativeRoute = currentVert.dist + currentVert.connectedTo[nbr]
                        if alternativeRoute < nbr.dist:
                            nbr.setDistance(alternativeRoute)
                            nbr.setPred(currentVert)
                            for element in listOfDistances:
                                if element[1] == nbr.id:
                                    element[0] = alternativeRoute

                path = []

                currentVert = end

                while currentVert.pred != None:
                    path.insert(0, currentVert.id)
                    currentVert = currentVert.pred
                if path:
                    path.insert(0, currentVert.id)
                for i in path:
                    currentVert = self.getVertex(i)

                length = 0
                for i in range(0, len(path) - 1):
                    j = i + 1
                    el = self.getVertex(path[i])
                    el1 = self.getVertex(path[j])
                    length += el.getWeight(el1)

                return length

            else:
                listOfElements = self.getVertices()
                listawynikow = ""
                for element in listOfElements:
                    listawynikow += (str(self.bfs(start, element)) + "\n")
                self.bfs(start, element)
                return listawynikow

    def dfs(self):
        topology = []
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex, topology)

        topological_sorted = []
        for i in topology:
            topological_sorted.insert(0, i.id)

        return topological_sorted

    def dfsvisit(self, startVertex, topology):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex, topology)
        startVertex.setColor('black')
        self.time += 1
        topology.append(startVertex)
        startVertex.setFinish(self.time)

    def traverse(self, start):
        result = []
        x = start
        while x.getPred():
            result.append(x.getId())
            x = x.getPred()
        result.append(x.getId())
        return result

    def showDistances(self, dist_vect):
        print("Distance from node: {}".format(self))
        for u in range(len(dist_vect)):
            if dist_vect[u] == sys.maxsize:
                d = None
            else:
                d = dist_vect[u]
            print('Node {} has distance: {}'.format(u, d))


#  functions using to count the shortest path
def dijkstra(graph, start):
    start = graph.getVertex(start)
    start.setDistance(0)
    start.setPred(None)

    # priority queue which contains tuple
    unvisited = [(v.getDistance(), v) for v in graph]
    unvisited = sorted(unvisited, key=lambda x: x[0])

    while len(unvisited):
        # Pop a vertex with the smallest distance
        vertex = unvisited.pop(0)
        current = vertex[1]
        current.visited = True

        # for next in v.adjacent:
        for next in current.connectedTo:
            # if visited, skip
            if next.visited:
                continue

            new = current.getDistance() + current.getWeight(next)
            if new < next.getDistance():
                next.setDistance(new)
                next.setPred(current)
            else:
                pass

        # Rebuild the unvisited list
        unvisited = [(v.getDistance(), v) for v in graph if not v.visited]
        unvisited = sorted(unvisited, key=lambda x: x[0])


def shortest(graph, target, path=None):
    if path == None:
        path = [target]
        target = graph.getVertex(target)

    if target.previous:
        path.append(target.previous.getId())
        shortest(graph, target.previous, path)

    return path[::-1]


def makePath(graph, start):
    start = graph.getVertex(start)
    if not start:
        raise Exception("This point is not defined in the graph")
    dijkstra(graph, start)
    path = {v: v.getDistance for v in graph.getVertices()}
    undiscovered = {v: None for v in graph.getVertices()}

    path.update(undiscovered)
    return path


if __name__ == '__main__':
    g = Graph()

    g.addEdge(6, 1, 5)
    g.addEdge(6, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(4, 6, 1)
    g.addEdge(3, 7, 2)
    g.addEdge(7, 4, 10)
    g.addEdge(5, 2, 10)
    g.addEdge(1, 3, 4)
    g.addEdge(4, 2, 2)
    g.addEdge(6, 7, 100)
    g.addEdge(10, 11, 1)


    print("Topological sort")
    print(g.dfs())

    print("Shortest Path")
    print(g.bfs('1'))


