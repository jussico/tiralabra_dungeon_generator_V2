
import random
from common.cell import *
from common.piste import *

# TODO: use this
class Base:

    def __init__(self):
        pass

    def solve(self, maze):
        print(f'@{self.__class__.__name__} solve_it() method.')
        self.maze = maze
        maze.reset()        
        maze.visualizer.reset()
        return self.solve_it(maze)

    def get_default_infomessages(self):
        infomessages = []
        # infomessages.append(f'visualizerr: {self.maze.visualizer.__class__.__name__}') 
        infomessages.append(f'solving class: {self.__class__.__name__}') 
        infomessages.append(f"start: {self.maze.alkupiste.pair()} end: {self.maze.loppupiste.pair()} frame: {self.maze.frame} framedrop: {self.maze.framedrop}")
        return infomessages

    def __str__(self):
        return self.__class__.__name__
