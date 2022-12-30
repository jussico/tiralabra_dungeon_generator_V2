
from common.cell import *
from common.piste import *
from common.neighbourg import *
import random
from abc import abstractmethod
from enum import IntEnum
# from visualizer.dummy import Dummy

class StartEndLocations(IntEnum):
  TopDownEnds = 1
  LeftRightEnds = 2
  
class Direction(IntEnum):
  UP = 0
  RIGHT = 1
  DOWN = 2
  LEFT = 3

class Maze:

  def __init__(self,leveys,korkeus, visualizer, interactive, framedrop, solving_name):
    self.korkeus = korkeus
    self.leveys = leveys
    self.visualizer = visualizer
    self.interactive = interactive
    self.taulukko = [[Cell() for _ in range(leveys)] for _ in range(korkeus)]
    self.possible_endpoints = []
    self.framedrop = int(framedrop)
    self.solving_name = solving_name
    self.frame = 0
    self.solved = False

    # randomize start point to one of the 4 edges. end point will be in the opposite edge.
    # randomize other (x or y) by the edge length.

    # TODO: how to just get all values
    possible_locations = [ StartEndLocations.TopDownEnds.value, StartEndLocations.LeftRightEnds.value ]
    selected_start_location = random.randrange(1, len(possible_locations)+1)
    # print(f"possible locations: {possible_locations} selected_location: {selected_start_location}")
    if selected_start_location == StartEndLocations.LeftRightEnds.value:
      x_positions = [0,leveys-1] # ok?
      random_x_position = random.randrange(0,2)
      start_x = x_positions[random_x_position]
      start_y = random.randrange(0,korkeus)
      end_x = x_positions[(random_x_position + 1) % len(x_positions)]
      end_y = -1 # undefined for now.
    else:
      y_positions = [0, korkeus-1] # ok?
      random_y_position = random.randrange(0,2)
      start_y = y_positions[random_y_position]
      start_x = random.randrange(0,leveys)
      end_x = -1 # undefined for now
      end_y = y_positions[(random_y_position + 1) % len(y_positions)]
    self.alkupiste = Point(start_x, start_y)
    self.loppupiste = Point(end_x, end_y)

  def reset(self):
    self.frame = 0
    self.solved = False
    for row in self.taulukko:
      for cell in row:
        cell.visited = False

  def generate_maze(self):
    print(f'@{self.__class__.__name__} generate_maze() method.')
    # algorithm implementation defined in subclass. ( DFS, etc. )
    return self.generate_with_endpoint(self.alkupiste.x, self.alkupiste.y)

  # NOTE: can't check visited here as they may change after one direction.
  def get_legal_neighbours(self, x, y, legal_directions):
    legal_neigbours = []
    for direction in legal_directions:
      if direction == Direction.UP:
          legal_neigbours.append(Neighbourg(x, y-1, Direction.UP))
      if direction == Direction.DOWN:
          legal_neigbours.append(Neighbourg(x, y+1, Direction.DOWN))
      if direction == Direction.RIGHT:
          legal_neigbours.append(Neighbourg(x+1, y, Direction.RIGHT))
      if direction == Direction.LEFT:
          legal_neigbours.append(Neighbourg(x-1, y, Direction.LEFT))
    return legal_neigbours

  # NOTE: can't check visited here as they may change after one direction.
  def get_legal_neighbours_for_solution(self, x, y, legal_directions):
    current = self.taulukko[y][x]
    legal_neigbours = []
    for direction in legal_directions:
      if direction == Direction.UP and not self.taulukko[y-1][x].wall_down:
          legal_neigbours.append(Neighbourg(x, y-1, Direction.UP))
      if direction == Direction.DOWN and not current.wall_down:
          legal_neigbours.append(Neighbourg(x, y+1, Direction.DOWN))
      if direction == Direction.RIGHT and not current.wall_right:
          legal_neigbours.append(Neighbourg(x+1, y, Direction.RIGHT))
      if direction == Direction.LEFT and not self.taulukko[y][x-1].wall_right:
          legal_neigbours.append(Neighbourg(x-1, y, Direction.LEFT))
    return legal_neigbours

  # get directions to neighboring cells within the borders of the maze
  def get_legal_directions(self, x, y):
    directions = []
    # print(f"self.leveys: {self.leveys} self.korkeus: {self.korkeus} x+1: {x+1}")
    if x - 1 >= 0:  directions.append(Direction.LEFT)
    if x + 1 < self.leveys: directions.append(Direction.RIGHT)
    if y - 1 >= 0:  directions.append(Direction.UP)
    if y + 1 < self.korkeus : directions.append(Direction.DOWN)
    return directions

  def is_within_limits(self, x, y):
    return x >= 0 and y >= 0 and x < self.leveys and y < self.korkeus

  def is_legal(self, current_coords, xdiff, ydiff):
    current_x = current_coords[0]
    current_y = current_coords[1]
    possible_x = current_coords[0] + xdiff
    possible_y = current_coords[1] + ydiff
    if not self.is_within_limits(possible_x, possible_y):
      return False
    if xdiff == 0:
      # DOWN
      if ydiff == 1 and not self.taulukko[current_y][current_x].wall_down:
        return True
      # UP
      if ydiff == -1 and not self.taulukko[possible_y][possible_x].wall_down:        
        return True
    elif ydiff == 0:
      # RIGHT
      if xdiff == 1 and not self.taulukko[current_y][current_x].wall_right:
        return True
      # LEFT
      if xdiff == -1 and not self.taulukko[possible_y][possible_x].wall_right:
        return True
  
  @abstractmethod
  def generate(self, korkeus, leveys):
    pass

  @abstractmethod
  def clear(self):
    pass

  def __str__(self):
    return f"{self.__class__.__name__}"
    # return f"{self.__class__.__name__} leveys: {self.leveys} korkeus: {self.korkeus} visualizer: {self.visualizer} \
    #   len(taulukko): {len(self.taulukko)} alkupiste: {self.alkupiste} loppupiste: {self.loppupiste} "
