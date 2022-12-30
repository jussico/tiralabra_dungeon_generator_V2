import sys
import random
from common.cell import *
from common.piste import *
from solving.base import Base

class MementoRandom(Base):

    def __init__(self):
        pass

    def solve_it(self, maze):
        maze.taulukko[self.maze.alkupiste.y][self.maze.alkupiste.x].visited = True

        maze.solved = False

        limit = sys.maxsize
        maze.frame = 0

        current = maze.alkupiste

        while not maze.solved and maze.frame < limit:
            maze.frame = maze.frame + 1

            if current == self.maze.loppupiste:
                maze.solved = True
                continue

            dirs = self.maze.get_legal_directions(current.x, current.y)

            random.shuffle(dirs)

            legal_neighbours = self.maze.get_legal_neighbours_for_solution(current.x, current.y, dirs)

            for neighbour in legal_neighbours:

                naapuri = neighbour.piste().pair()

                if naapuri == self.maze.loppupiste.pair():
                    maze.solved = True
                    continue

                # for visualization only
                maze.taulukko[neighbour.y][neighbour.x].visited = True

                # if solved or frame % 1000 == 0:
                infomessages = self.get_default_infomessages()
                infomessages.append(f"current: {current}")
                infomessages.append(f"neighbour: {neighbour}")
                self.maze.visualizer.visualize(self.maze, infomessages)
                # if maze.interactive: input(f"pressi enter. counter: {maze.frame}")

                current = neighbour

        return maze.solved
