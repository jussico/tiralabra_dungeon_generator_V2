
import random
from common.cell import *
from common.piste import *
from solving.base import Base
import heapq

# TODO: fix
class AstarJumpPoint(Base):

    def __init__(self):
        pass

    def solve_it(self, maze):

        self.maze = maze
        maze.reset_visited()

        queue = []
        heapq.heappush(queue, (0, maze.alkupiste.pair()))
        cost = { maze.alkupiste.pair(): 0 }
        parent = {maze.alkupiste.pair(): None}
        visited = set()
        previous_node = None

        while queue:            
            current_cost, current_node = heapq.heappop(queue)

            if current_node == maze.loppupiste.pair():
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = parent[current_node]
                return path[::-1]
            
            visited.add(current_node)
            # for visualisation
            maze.taulukko[current_node[1]][current_node[0]].visited = True

            # jump ahead if possible
            print(f"previous_node: {previous_node} current_node: {current_node}")
            if previous_node:
                pass
                xdiff, ydiff = current_node[0] - previous_node[0], current_node[1] - previous_node[1]
                print(f"jumping! differences to previous: xdiff: {xdiff} ydiff: {ydiff}")
                while self.maze.is_legal(current_node, xdiff, ydiff):
                    next = (current_node[0] + xdiff, current_node[1] + ydiff)
                    parent[next] = current_node
                    cost[next] = cost[current_node] + 1
                    previous_node = current_node
                    current_node = next

                    # for visualisation
                    maze.taulukko[current_node[1]][current_node[0]].visited = True                    
                    infomessages = []
                    infomessages.append(f"start: {maze.alkupiste}")
                    infomessages.append(f"end: {maze.loppupiste}")
                    infomessages.append(f"current: {current_node}")
                    infomessages.append(f"neighbour: {neighbour}")
                    maze.visualizer.visualize(maze, infomessages)
                    input("continue middle of jump.")      

                    if current_node == maze.loppupiste.pair():
                        return True

            input("continue from after jump.")


            dirs = maze.get_legal_directions(current_node[0], current_node[1])

            legal_neighbours = maze.get_legal_neighbours_for_solution(current_node[0], current_node[1], dirs)            

            for neighbour in legal_neighbours:
                naapuri = neighbour.piste().pair()
                if naapuri in visited:
                    continue
                neighbour_cost = cost[current_node] + 1
                if naapuri not in cost or neighbour_cost < cost[naapuri]:
                    cost[naapuri] = neighbour_cost
                    priority = neighbour_cost + self.euclidean_distance(maze.loppupiste.pair(), naapuri)
                    heapq.heappush(queue, (priority, naapuri))
                    parent[naapuri] = current_node
                    infomessages = []
                    infomessages.append(f"start: {maze.alkupiste}")
                    infomessages.append(f"end: {maze.loppupiste}")
                    infomessages.append(f"current: {current_node}")
                    infomessages.append(f"neighbour: {neighbour}")
                    # infomessages.append(f"queue: {queue}") # prints too much..
                    maze.visualizer.visualize(maze, infomessages)
                    # input("pressi enter.")      

            previous_node = current_node                                  
        return None

    def euclidean_distance(self, a,b):
        row1, col1 = a
        row2, col2 = b
        return ((row1 - row2) ** 2 + (col1 - col2) ** 2) ** 0.5
