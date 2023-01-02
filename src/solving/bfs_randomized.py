
import random
from common.cell import *
from common.point import *
from solving.bfs import Bfs

class BfsRandomized(Bfs):

    # overrides Bfs class method
    def get_directions(self, x, y):
        directions = self.maze.get_legal_directions(x, y)
        random.shuffle(directions)
        return directions
