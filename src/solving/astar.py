
import random
from common.cell import *
from common.point import *
import heapq
from solving.base import Base

class Astar(Base):

    def solve_it(self, maze):
        queue = []
        heapq.heappush(queue, (0, maze.starting_point.pair()))
        cost = { maze.starting_point.pair(): 0 }
        parent = {maze.starting_point.pair(): None}
        visited = set()

        while queue:

            maze.frame = maze.frame + 1

            current_cost, current_node = heapq.heappop(queue)

            if current_node == maze.ending_point.pair():
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent[current_node]
                maze.solved = True
                self.maze.visualizer.visualize(self.maze, self.get_default_infomessages())                

                return True, path[::-1]
            
            visited.add(current_node)
            # for visualisation
            maze.taulukko[current_node[1]][current_node[0]].visited = True

            dirs = maze.get_legal_directions(current_node[0], current_node[1])

            legal_neighbours = maze.get_legal_neighbours_for_solution(current_node[0], current_node[1], dirs)            

            for neighbour in legal_neighbours:
                naapuri = neighbour.piste().pair()
                if naapuri in visited:
                    continue
                neighbour_cost = cost[current_node] + 1
                if naapuri not in cost or neighbour_cost < cost[naapuri]:
                    cost[naapuri] = neighbour_cost
                    priority = neighbour_cost + self.euclidean_distance(maze.ending_point.pair(), naapuri)
                    heapq.heappush(queue, (priority, naapuri))
                    parent[naapuri] = current_node
                    infomessages = self.get_default_infomessages()
                    infomessages.append(f"current: {current_node}")
                    infomessages.append(f"neighbour: {neighbour}")
                    # infomessages.append(f"queue: {queue}") # prints too much..
                    maze.visualizer.visualize(maze, infomessages)
                    # input("pressi enter.")                                        
        return False, None

    def euclidean_distance(self, a,b):
        row1, col1 = a
        row2, col2 = b
        return ((row1 - row2) ** 2 + (col1 - col2) ** 2) ** 0.5

    def __str__(self):
        return self.__class__.__name__
