
import random
from common.cell import *
from common.point import *

from solving.base import Base

class Bfs(Base):

    def __init__(self):
        pass

    def solve_it(self, maze):
        queue = []

        queue.append(maze.starting_point.pair())

        self.maze.taulukko[self.maze.starting_point.y][self.maze.starting_point.x].visited = True

        maze.solved = False

        prev_pos = {}
        prev_pos[maze.starting_point.pair()] = None

        while queue and not maze.solved:

            maze.frame = maze.frame + 1

            current = queue.pop(0)

            if current == self.maze.ending_point.pair():
                maze.solved = True
                self.maze.visualizer.visualize(self.maze, self.get_default_infomessages())                
                continue

            directions = self.get_directions(current[0], current[1])

            random.shuffle(directions)

            legal_neighbours = self.maze.get_legal_neighbours_for_solution(current[0], current[1], directions)

            for neighbour in legal_neighbours:
                if not self.maze.taulukko[neighbour.y][neighbour.x].visited:
                    naapuri = neighbour.pair()

                    queue.append(naapuri)
                    self.maze.taulukko[neighbour.y][neighbour.x].visited = True
                    prev_pos[naapuri] = current

                    infomessages = self.get_default_infomessages()
                    infomessages.append(f"current: {current}")
                    self.maze.visualizer.visualize(self.maze, infomessages)

        if maze.solved:
            solution = []
            curr_pos = maze.ending_point.pair()
            while curr_pos != maze.starting_point.pair():
                solution.append(curr_pos)
                curr_pos = prev_pos[curr_pos]
            solution.append(maze.starting_point.pair())
            solution = solution[::-1]            
        else:
            solution = None

        return maze.solved, solution

    def get_directions(self, x, y):
        directions = self.maze.get_legal_directions(x, y)
        return directions

    def __str__(self):
        return self.__class__.__name__
