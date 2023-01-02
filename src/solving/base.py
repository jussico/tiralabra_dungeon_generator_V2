
from common.cell import *
from common.point import *

class Base:

    def __init__(self):
        pass

    def solve(self, maze):
        print(f'@{self.__class__.__name__} solve() method.')
        self.maze = maze
        maze.reset()        
        maze.visualizer.reset()
        solved_boolean, possible_route = self.solve_it(maze)
        return solved_boolean, possible_route

    def get_default_infomessages(self):
        infomessages = []
        infomessages.append(f'solving class: {self.__class__.__name__}') 
        infomessages.append(f"start: {self.maze.starting_point.pair()} end: {self.maze.ending_point.pair()} frame: {self.maze.frame} framedrop: {self.maze.framedrop}")
        return infomessages

    def __str__(self):
        return self.__class__.__name__
