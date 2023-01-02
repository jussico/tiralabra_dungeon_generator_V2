
import random
from common.cell import *
from common.point import *
from common.maze import *
import sys
from solving.base import Base

class WallFollower(Base):

    def solve_it(self, maze):
        self.maze = maze

        self.maze.taulukko[self.maze.starting_point.y][self.maze.starting_point.x].visited = True

        maze.solved = False

        # figure out direction at start
        if(maze.starting_point.x == 0 or maze.starting_point.y == 0):
            direction = Direction.UP
        else:
            direction = Direction.DOWN

        if maze.interactive: input(f"direction alussa: {direction}")

        current = Neighbourg(self.maze.starting_point.x, self.maze.starting_point.y, direction)

        # limit max to visiting each cell twice
        limit = maze.leveys * maze.korkeus * 2

        counter = 0

        while not maze.solved and counter < limit:

            maze.frame = maze.frame + 1

            counter = counter + 1

            if current.pair() == self.maze.ending_point.pair():
                maze.solved = True
                self.maze.visualizer.visualize(self.maze, self.get_default_infomessages())                
                continue

            neighbourg = self.get_next_neighbourg_left_from_direction(current, direction)

            # for visualization only
            self.maze.taulukko[neighbourg.y][neighbourg.x].visited = True

            infomessages = self.get_default_infomessages()
            infomessages.append(f"current: {current}")
            infomessages.append(f"direction: {direction}")
            infomessages.append(f"neighbour: {neighbourg}")
            maze.visualizer.visualize(maze, infomessages)            

            direction = neighbourg.direction
            current = neighbourg

        return maze.solved, None

    def get_next_neighbourg_left_from_direction(self, current, current_direction):

        x = current.x
        y = current.y

        legal_directions = self.maze.get_legal_directions(x, y)

        left, left_good = (Neighbourg(x-1, y, Direction.LEFT), not self.maze.taulukko[y][x-1].wall_right)
        right, right_good = (Neighbourg(x+1, y, Direction.RIGHT), not self.maze.taulukko[y][x].wall_right)
        down, down_good = (Neighbourg(x, y+1, Direction.DOWN), not self.maze.taulukko[y][x].wall_bottom)
        up, up_good = (Neighbourg(x, y-1, Direction.UP), not self.maze.taulukko[y-1][x].wall_bottom)
        next = None
        if current_direction == Direction.UP:
            if Direction.LEFT in legal_directions and left_good:
                next = left
            elif Direction.UP in legal_directions and up_good:
                next = up
            elif Direction.RIGHT in legal_directions and right_good:
                next = right
            elif Direction.DOWN in legal_directions and down_good:
                next = down
        elif current_direction == Direction.RIGHT:
            if Direction.UP in legal_directions and up_good:
                next = up
            elif Direction.RIGHT in legal_directions and right_good:
                next = right
            elif Direction.DOWN in legal_directions and down_good:
                next = down
            elif Direction.LEFT in legal_directions and left_good:
                next = left
        elif current_direction == Direction.DOWN:
            if Direction.RIGHT in legal_directions and right_good:
                next = right
            elif Direction.DOWN in legal_directions and down_good:
                next = down
            elif Direction.LEFT in legal_directions and left_good:
                next = left
            elif Direction.UP in legal_directions and up_good:
                next = up
        elif current_direction == Direction.LEFT:
            if Direction.DOWN in legal_directions and down_good:
                next = down
            elif Direction.LEFT in legal_directions and left_good:
                next = left
            elif Direction.UP in legal_directions and up_good:
                next = up
            elif Direction.RIGHT in legal_directions and right_good:
                next = right        
        return next

    def __str__(self):
        return self.__class__.__name__
