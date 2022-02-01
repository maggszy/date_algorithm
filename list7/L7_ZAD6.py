from L7_ZAD3 import Graph


class State:
    def __init__(self, cannibal_left, missionary_left, boat, cannibal_right, missionary_right):
        self.cannibal_left = cannibal_left
        self.missionary_left = missionary_left
        self.boat = boat
        self.cannibal_right = cannibal_right
        self.missionary_right = missionary_right
        self.parent = None
        self.text = (str(cannibal_left) + " " + str(missionary_left) + " " + str(boat))

    def is_goal(self):
        if self.cannibal_left == 0 and self.missionary_left == 0:
            return True
        else:
            return False

    def is_valid(self):
        if self.missionary_left >= 0 and self.missionary_right >= 0 \
                and self.cannibal_left >= 0 and self.cannibal_right >= 0 \
                and (self.missionary_left == 0 or self.missionary_left >= self.cannibal_left) \
                and (self.missionary_right == 0 or self.missionary_right >= self.cannibal_right):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.cannibal_left == other.cannibal_left and self.missionary_left == other.missionary_left \
               and self.boat == other.boat and self.cannibal_right == other.cannibal_right \
               and self.missionary_right == other.missionary_right

    def __hash__(self):
        return hash((self.cannibal_left, self.missionary_left, self.boat, self.cannibal_right, self.missionary_right))


class RiverProblem(Graph):
    def __init__(self):
        self.photo = 1
        self.children = []
        self.vertList = {}
        self.numVertices = 0

    def successors(self, current):
        children = []

        if current.boat == 0:
            new_state = State(current.cannibal_left, current.missionary_left - 2, 1,
                              current.cannibal_right, current.missionary_right + 2)

            if new_state.is_valid():  # (2, 0, 1)
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left - 2, current.missionary_left, 1,
                              current.cannibal_right + 2, current.missionary_right)

            if new_state.is_valid():  # (0, 2, 1)
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left - 1, current.missionary_left - 1, 1,
                              current.cannibal_right + 1, current.missionary_right + 1)

            if new_state.is_valid():  # (1, 1, 1)
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left, current.missionary_left - 1, 1,
                              current.cannibal_right, current.missionary_right + 1)

            if new_state.is_valid():  # (1, 0, 1)
                new_state.parent = current
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left - 1, current.missionary_left, 1,
                              current.cannibal_right + 1, current.missionary_right)

            if new_state.is_valid():  # (0, 1, 1)
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)

        else:
            new_state = State(current.cannibal_left, current.missionary_left + 2, 0,
                              current.cannibal_right, current.missionary_right - 2)

            if new_state.is_valid():  # (2, 0, 0)
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left + 2, current.missionary_left, 0,
                              current.cannibal_right - 2, current.missionary_right)

            if new_state.is_valid():  # (0, 2, 0)
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left + 1, current.missionary_left + 1, 0,
                              current.cannibal_right - 1, current.missionary_right - 1)
            ## One missionary and one cannibal cross right to left.
            if new_state.is_valid():
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left, current.missionary_left + 1, 0,
                              current.cannibal_right, current.missionary_right - 1)
            ## One missionary crosses right to left.
            if new_state.is_valid():
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)
            new_state = State(current.cannibal_left + 1, current.missionary_left, 0,
                              current.cannibal_right - 1, current.missionary_right)
            ## One cannibal crosses right to left.
            if new_state.is_valid():
                new_state.parent = current
                children.append(new_state)
                self.addEdge(current.text, new_state.text, 1)

        return children

    def finding_a_solution(self):
        initial_state = State(3, 3, 0, 0, 0)
        if initial_state.is_goal():
            return initial_state
        l = list()
        explored = set()
        l.append(initial_state)
        while l:
            state = l.pop(0)
            if state.is_goal():
                return state
            explored.add(state)
            children = self.successors(state)
            for child in children:
                if (child not in explored) or (child not in l):
                    l.append(child)
        return None

    def print_solution(self, solution):
        path = []
        path.append(solution)
        parent = solution.parent
        while parent:
            path.append(parent)
            parent = parent.parent

        for t in range(len(path)):
            state = path[len(path) - t - 1]
            print("(" + str(state.cannibal_left) + "," + str(state.missionary_left) \
                  + "," + str(state.boat) + "," + str(state.cannibal_right) + "," + \
                  str(state.missionary_right) + ")")


def main():
    g = RiverProblem()
    g.print_solution(g.finding_a_solution())


if __name__ == "__main__":
    main()
