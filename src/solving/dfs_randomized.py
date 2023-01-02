
import random
from common.cell import *
from common.point import *
from solving.dfs import Dfs

class DfsRandomized(Dfs):

    # overrides Dfs method
    def get_directions(self, x, y):
        directions = self.maze.get_legal_directions(x, y)    
        random.shuffle(directions)        
        return directions
