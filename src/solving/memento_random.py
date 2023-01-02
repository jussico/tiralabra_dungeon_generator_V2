import sys
import random
from common.cell import *
from common.point import *
from solving.base import Base

class MementoRandom(Base):

    def __init__(self):
        pass

    def solve_it(self, maze):
        maze.taulukko[self.maze.starting_point.y][self.maze.starting_point.x].visited = True

        maze.solved = False

        # limit = 1000
        # limit = sys.maxsize
        limit = maze.leveys * maze.korkeus * 1000 # wont take forever
        maze.frame = 0

        current = maze.starting_point

        while not maze.solved and maze.frame < limit:
            maze.frame = maze.frame + 1

            if current == self.maze.ending_point:
                maze.solved = True
                continue

            dirs = self.maze.get_legal_directions(current.x, current.y)

            random.shuffle(dirs)

            legal_neighbours = self.maze.get_legal_neighbours_for_solution(current.x, current.y, dirs)

            for neighbour in legal_neighbours:

                naapuri = neighbour.piste().pair()

                if naapuri == self.maze.ending_point.pair():
                    maze.solved = True
                    continue

                maze.taulukko[neighbour.y][neighbour.x].visited = True

                infomessages = self.get_default_infomessages()
                infomessages.append(f"current: {current}")
                infomessages.append(f"neighbour: {neighbour}")
                self.maze.visualizer.visualize(self.maze, infomessages)

                current = neighbour

        return maze.solved, None
