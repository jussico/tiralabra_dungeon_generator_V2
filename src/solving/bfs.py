
import random
from common.cell import *
from common.piste import *

from solving.base import Base

class Bfs(Base):

    def __init__(self):
        pass

    def solve_it(self, maze):
        queue = []

        queue.append(maze.alkupiste)

        self.maze.taulukko[self.maze.alkupiste.y][self.maze.alkupiste.x].visited = True

        maze.solved = False

        prev_pos = {}
        prev_pos[maze.alkupiste] = None

        while queue and not maze.solved:

            maze.frame = maze.frame + 1

            current = queue.pop(0)

            if current.pair() == self.maze.loppupiste.pair():
                maze.solved = True
                # infomessages.append(f"neighbour: {neighbour}")
                # infomessages.append(f"queue: {queue}")
                self.maze.visualizer.visualize(self.maze, self.get_default_infomessages())                
                continue

            directions = self.get_directions(current)

            random.shuffle(directions)

            legal_neighbours = self.maze.get_legal_neighbours_for_solution(current.x, current.y, directions)

            for neighbour in legal_neighbours:
                if not self.maze.taulukko[neighbour.y][neighbour.x].visited:

                    queue.append(neighbour)
                    self.maze.taulukko[neighbour.y][neighbour.x].visited = True
                    prev_pos[neighbour] = current

                    infomessages = self.get_default_infomessages()
                    infomessages.append(f"current: {current}")
                    # infomessages.append(f"neighbour: {neighbour}")
                    # infomessages.append(f"queue: {queue}")
                    self.maze.visualizer.visualize(self.maze, infomessages)
                    # if maze.interactive: input("press enter to continue.")

        # if solved:
        #     solution = []
        #     curr_pos = maze.loppupiste
        #     while curr_pos != maze.alkupiste:
        #         solution.append(curr_pos)
        #         curr_pos = prev_pos[curr_pos]
        #     solution.append(maze.alkupiste)
        #     return solution[::-1]            

        return maze.solved

    def get_directions(self, current):
        directions = self.maze.get_legal_directions(current.x, current.y)
        return directions

    def __str__(self):
        return self.__class__.__name__
