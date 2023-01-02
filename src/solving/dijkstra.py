
import random
from common.cell import *
from common.point import *
from heapq import heappush, heappop
from solving.base import Base

class Dijkstra(Base):

    def solve_it(self, maze):
        distances = {}
        previous = {}
        for i in range(maze.leveys):
            for j in range(maze.korkeus):
                distances[(i,j)] = float("inf")
                previous[(i,j)] = None
        distances[maze.starting_point.pair()] = 0

        heap = []
        heappush(heap, (0, maze.starting_point.pair()))

        while heap:

            maze.frame = maze.frame + 1

            distance, cell = heappop(heap)

            if cell == maze.ending_point.pair():
                path = []
                while cell:
                    path.append(cell)
                    cell = previous[cell]
                maze.solved = True
                self.maze.visualizer.visualize(self.maze, self.get_default_infomessages())

                return True, path[::-1]

            dirs = self.maze.get_legal_directions(cell[0], cell[1])

            legal_neighbours = self.maze.get_legal_neighbours_for_solution(cell[0], cell[1], dirs)   

            for neighbour in legal_neighbours:
                self.maze.taulukko[neighbour.y][neighbour.x].visited = True
                naapuri = neighbour.piste().pair()
                new_distance = distance + 1
                if new_distance < distances[naapuri]:
                    distances[naapuri] = new_distance
                    previous[naapuri] = cell
                    heappush(heap, (new_distance, naapuri))

                    infomessages = self.get_default_infomessages()
                    infomessages.append(f"current: {cell}")
                    self.maze.visualizer.visualize(self.maze, infomessages)
        
        return False, None

    def __str__(self):
        return self.__class__.__name__
