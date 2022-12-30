
import random
from common.cell import *
from common.piste import *
from solving.bfs import Bfs

class BfsRandomized(Bfs):

    # overrides Bfs method
    def get_directions(self, current):
        directions = self.maze.get_legal_directions(current.x, current.y)
        random.shuffle(directions)
        return directions
