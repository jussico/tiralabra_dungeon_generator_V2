
from common.cell import *
from common.piste import *
from common.neighbourg import *
import random
from abc import abstractmethod

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Maze:

  def __init__(self,leveys,korkeus, visualizer):
    self.korkeus = korkeus
    self.leveys = leveys
    self.visualizer = visualizer
    self.taulukko = [[Cell() for _ in range(leveys)] for _ in range(korkeus)]

    # TODO: randomize start and end point to opposite outer walls

    self.alkupiste = Piste(random.randrange(leveys), random.randrange(korkeus))
    self.loppupiste = Piste(random.randrange(leveys), random.randrange(korkeus))

    # visualizer.clear()

    # algorithm implementation defined in subclass. ( DFS, etc. )
    self.generate(self.alkupiste.x, self.alkupiste.y)

  # NOTE: can't check visited here as they may change after one direction.
  def get_legal_neighbours(self, x, y, legal_directions):
    legal_neigbours = []
    for direction in legal_directions:
      if direction == UP:
          legal_neigbours.append(Neighbourg(x, y-1, UP))
      if direction == DOWN:
          legal_neigbours.append(Neighbourg(x, y+1, DOWN))
      if direction == RIGHT:
          legal_neigbours.append(Neighbourg(x+1, y, RIGHT))
      if direction == LEFT:
          legal_neigbours.append(Neighbourg(x-1, y, LEFT))
    return legal_neigbours

  # get directions to neighboring cells within the borders of the maze
  def get_legal_directions(self, x, y):
    directions = []
    if x - 1 >= 0:  directions.append(LEFT)
    if x + 1 <= self.leveys - 1: directions.append(RIGHT)
    if y - 1 >= 0:  directions.append(UP)
    if y + 1 <= self.korkeus - 1: directions.append(DOWN)
    return directions
  
  @abstractmethod
  def generate(self, korkeus, leveys):
    pass

  @abstractmethod
  def clear(self):
    pass
