
import random
from common.cell import *
from common.piste import *
from heapq import heappush, heappop
from solving.base import Base

class Dijkstra(Base):

    def solve_it(self, maze):
        distances = {}
        previous = {}
        for i in range(len(maze.taulukko)):
            for j in range(len(maze.taulukko[0])):
                distances[(i,j)] = float("inf")
                previous[(i,j)] = None
        distances[maze.alkupiste.pair()] = 0

        heap = []
        heappush(heap, (0, maze.alkupiste.pair()))

        while heap:

            maze.frame = maze.frame + 1

            distance, cell = heappop(heap)

            if cell == maze.loppupiste.pair():
                path = []
                while cell:
                    path.append(cell)
                    cell = previous[cell]
                maze.solved = True
                self.maze.visualizer.visualize(self.maze, self.get_default_infomessages())

                return path[::-1]

            dirs = self.maze.get_legal_directions(cell[0], cell[1])

            legal_neighbours = self.maze.get_legal_neighbours_for_solution(cell[0], cell[1], dirs)            

            for neighbour in legal_neighbours:
                self.maze.taulukko[neighbour.y][neighbour.x].visited = True
                naapuri = neighbour.piste().pair()
                new_distance = distance + 1
                # if new_distance < distances[naapuri]:
                if naapuri in distances and new_distance < distances[naapuri]:
                    distances[naapuri] = new_distance
                    previous[naapuri] = cell
                    # print(f"tyypit new_distance: {type(new_distance)} naapuri: {type(naapuri)}")
                    heappush(heap, (new_distance, naapuri))

                    infomessages = self.get_default_infomessages()
                    infomessages.append(f"current: {cell}")
                    # infomessages.append(f"neighbour: {neighbour}")
                    # infomessages.append(f"heap: {heap}")
                    self.maze.visualizer.visualize(self.maze, infomessages)
                    # if maze.interactive: input("press enter.")                    
        
        return None

    def __str__(self):
        return self.__class__.__name__
