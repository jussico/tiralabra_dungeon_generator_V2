
import random
from common.cell import *
from common.piste import *

from solving.base import Base

class Dfs(Base):

    def __init__(self):
        # maze.visualizer.visualize(maze, ["hellurei"])
        # exit(0)
        pass

    def solve_it(self, maze):
        self.maze = maze
        maze.reset()

        # Initialize a stack to store the path
        stack = []

        # Add the starting position to the stack
        stack.append(self.maze.alkupiste)

        # Mark the starting position as visited
        # maze[start[0]][start[1]] = 'V'
        self.maze.taulukko[self.maze.alkupiste.y][self.maze.alkupiste.x].visited = True

        # Initialize a flag to indicate if the maze has been solved
        maze.solved = False

        # print(f"stack == True: {stack == True}")
        # print(f"solved == True: {solved == True}")
        # exit(0)

        # Keep searching until the maze is solved or the stack is empty
        while stack and not maze.solved:
            maze.frame = maze.frame + 1
            # Get the current position from the top of the stack
            # curr_row, curr_col = stack[-1]
            current = stack[-1]

            # Check if the current position is the end position
            if current.pair() == self.maze.loppupiste.pair():
                maze.solved = True
                continue

            directions = self.get_directions(current)

            legal_neighbours = self.maze.get_legal_neighbours_for_solution(current.x, current.y, directions)

            # infomessages = []
            infomessages = self.get_default_infomessages()
            # infomessages.append(f"start: {self.maze.alkupiste}")
            # infomessages.append(f"end: {self.maze.loppupiste}")
            infomessages.append(f"current: {current}")
            # infomessages.append(f"dirs: {directions}")
            # infomessages.append(f"legal_neighbours: {legal_neighbours}")
            # infomessages.append(f"stack: {stack}")
            self.maze.visualizer.visualize(self.maze, infomessages)
            #if(self.maze.interactive): input("press enter to continue.")

            continue_stack_loop = False
            for neighbour in legal_neighbours:
                if not self.maze.taulukko[neighbour.y][neighbour.x].visited:
                    #maze.generate(neighbour.x, neighbour.y, neighbour.direction)
                    # stack.append(Piste(neighbour.x, neighbour.y))

                    # exit(0)

                    stack.append(neighbour)
                    self.maze.taulukko[neighbour.y][neighbour.x].visited = True
                    # neighbour.visited = True

                    infomessages = self.get_default_infomessages()
                    infomessages.append(f"start: {self.maze.alkupiste}")
                    infomessages.append(f"end: {self.maze.loppupiste}")
                    infomessages.append(f"current: {current}")
                    # infomessages.append(f"neighbour: {neighbour}")
                    # infomessages.append(f"stack: {stack}")
                    self.maze.visualizer.visualize(self.maze, infomessages)
                    # if(self.maze.interactive): input("pressi enter.")

                    continue_stack_loop = True

            if continue_stack_loop:
                continue

            # If none of the moves are possible, backtrack by removing the current position from the stack
            stack.pop()

            infomessages = self.get_default_infomessages()
            infomessages.append(f"current: {current}")
            # infomessages.append(f"neighbour: {neighbour}")
            # infomessages.append(f"stack: {stack}")
            self.maze.visualizer.visualize(self.maze, infomessages)
            # if(self.maze.interactive): input("pressiiiii enter.")


        infomessages = []
        if maze.solved: 
            infomessages.append('maze solved.')
        else:
            infomessages.append('no solution found for maze.')

        self.maze.visualizer.visualize(self.maze, infomessages)

        return maze.solved

    def get_directions(self, current):
        directions = self.maze.get_legal_directions(current.x, current.y)
        return directions

    def __str__(self):
        return self.__class__.__name__