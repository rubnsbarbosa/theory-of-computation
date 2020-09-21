class State:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v):
        self.neighbors.append(v)

    