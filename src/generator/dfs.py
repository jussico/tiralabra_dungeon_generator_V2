
from common.cell import *
from common.piste import *
from common.maze import *
import random

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class DfsGenerator(Maze):

  def __init__(self,leveys,korkeus, visualizer):
    super().__init__(leveys, korkeus, visualizer)
  
  # generates the self.taulukko with depth-first algorithm
  def generate(self, x, y, direction = None):
    
    # TODO: dont always visualize
    infomessages = []
    infomessages.append(f'x: {x} y: {y}')
    infomessages.append(f'direction: {direction}')
    # self.visualizer.visualize(self, x, y, direction)
    self.visualizer.visualize(self, infomessages)
    # TODO: move to visualizer(s)
    input("Press Enter to continue...")

    self.taulukko[y][x].visited = True

    # delete walls between this and previous coordinates
    if direction == UP: 
      self.taulukko[y][x].wall_down = False
    elif direction == DOWN: 
      self.taulukko[y-1][x].wall_down = False
    elif direction == RIGHT: 
      self.taulukko[y][x-1].wall_right = False
    elif direction == LEFT: 
      self.taulukko[y][x].wall_right = False

    dirs = self.get_legal_directions(x, y)

    random.shuffle(dirs)

    legal_neighbours = self.get_legal_neighbours(x, y, dirs)

    for neighbour in legal_neighbours:
      if not self.taulukko[neighbour.y][neighbour.x].visited:
        self.generate(neighbour.x, neighbour.y, neighbour.direction)
