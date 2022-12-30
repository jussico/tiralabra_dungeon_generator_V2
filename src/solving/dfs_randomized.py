
import random
from common.cell import *
from common.piste import *
from solving.dfs import Dfs

class DfsRandomized(Dfs):

    # overrides Dfs method
    def get_directions(self, current):
        directions = self.maze.get_legal_directions(current.x, current.y)
        random.shuffle(directions)        
        return directions
