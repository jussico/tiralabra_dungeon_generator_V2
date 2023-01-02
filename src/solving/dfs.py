
import random
from common.cell import *
from common.point import *

from solving.base import Base

class Dfs(Base):

    def __init__(self):
        pass

    def solve_it(self, maze):
        self.maze = maze
        maze.reset()

        stack = [maze.starting_point.pair()]
        visited = set()

        while stack:
            x, y = stack.pop()
            visited.add((x,y))
            self.maze.taulukko[y][x].visited = True
            infomessages = self.get_default_infomessages()
            infomessages.append(f"current: {x},{y}")
            self.maze.visualizer.visualize(self.maze, infomessages)            
            if (x,y) == maze.ending_point.pair():
                self.maze.solved = True
                infomessages = self.get_default_infomessages()
                infomessages.append(f"current: {x},{y}")
                self.maze.visualizer.visualize(self.maze, infomessages)                            
                return self.maze.solved, self.get_path(visited)

            directions = self.get_directions(x, y)
            legal_neighbours = self.maze.get_legal_neighbours_for_solution(x, y, directions)

            for neighbourg in legal_neighbours:
                if not self.maze.taulukko[neighbourg.y][neighbourg.x].visited:
                    naapuri = neighbourg.pair()        
                    stack.append(naapuri)

        return self.maze.solved, None

    def get_path(self, visited):
        path = []
        for row, col in visited:
            path.append((row, col))
        return path[::-1]

    def get_directions(self, x, y):
        directions = self.maze.get_legal_directions(x, y)
        return directions

    def __str__(self):
        return self.__class__.__name__