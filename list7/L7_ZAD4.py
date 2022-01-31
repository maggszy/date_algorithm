from L7_ZAD3 import Graph


class Stack:
    """
    Klasa implementująca stos używając pythonowych list.
    """

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


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        """ Modification of dfs to return a list in topological sort order """
        topological_stack = []

        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex, topological_stack)

        return topological_stack

    def dfsvisit(self, startVertex, topological_stack):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex, topological_stack)

        startVertex.setColor('black')
        self.time += 1
        topological_stack.append(startVertex)
        startVertex.setFinish(self.time)


g = DFSGraph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)


print("Following is a Topological Sort of the given graph")
print(g.dfs())
