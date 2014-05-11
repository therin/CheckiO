
def checkio(labyrinth):
    class Cell(object):
        def __init__(self, x, y, reachable):
        """
        Initialize new cell

        @param x cell x coordinate
        @param y cell y coordinate
        @param reachable is cell reachable? not a wall?
        """
            self.reachable = reachable
            self.x = x
            self.y = y
            self.parent = None
            self.g = 0
            self.h = 0
            self.f = 0
    class AStar(object):
        def __init__(self):
            self.op = []
            heapq.heapify(self.op)
            self.cl = set()
            self.cells = []
            self.gridHeight = 12
            self.gridWidth = 12


checkio([
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,1,0,1,1,1],
[1,0,1,0,0,0,0,0,0,0,0,1],
[1,0,1,0,1,1,1,1,1,1,0,1],
[1,0,1,0,1,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,1,1,1,0,1],
[1,0,1,0,0,0,0,1,0,1,1,1],
[1,0,1,1,0,1,0,0,0,0,0,1],
[1,0,1,0,0,1,1,1,1,1,0,1],
[1,0,0,0,1,1,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
])