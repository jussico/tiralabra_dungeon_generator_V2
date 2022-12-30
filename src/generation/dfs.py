
from common.cell import *
from common.piste import *
from common.maze import *
import random

class DfsGenerator(Maze):

  # def __init__(self,leveys,korkeus, visualizer, interactive):
  #   super().__init__(leveys, korkeus, visualizer, interactive)
  
  def generate_with_endpoint(self, x, y, direction = None):

    # print(f"endpoint: {self.loppupiste}")

    self.generate(x, y, direction = None)

    # select endpoint from list of possible endpoints
    #print(f"possible endpoints: {self.possible_endpoints}")
    random_end_point_pair = self.possible_endpoints[random.randrange(0,len(self.possible_endpoints))]
    self.loppupiste = Point(random_end_point_pair[0], random_end_point_pair[1])

    # final draw after maze fully generated
    infomessages = [ "maze generation finished." ]

    # infomessages.append(f"possible endpoints: {self.possible_endpoints}")
    # infomessages.append[f"possible endpoints: {self.possible_endpoints[:]}"]
    # infomessages.append(f"endpoint: {self.loppupiste}")

    # infomessages.append(f'x: {x} y: {y}')
    self.visualizer.visualize(self, infomessages)

    return self

  # generates the self.taulukko with depth-first algorithm
  def generate(self, x, y, direction = None):
    
    # TODO: dont always visualize
    infomessages = []
    infomessages.append(f'x: {x} y: {y} direction: {direction}')
    # self.visualizer.visualize(self, x, y, direction)
    self.visualizer.visualize(self, infomessages)
    # TODO: move to visualizer(s)
    # input("Press Enter to continue...")


    stack = []
    stack.append(self.alkupiste)
    self.taulukko[y][x].visited = True

    while stack:
      current = stack[-1]

      dirs = self.get_legal_directions(current.x, current.y)

      random.shuffle(dirs)

      legal_neighbours = self.get_legal_neighbours(current.x, current.y, dirs)      

      continue_stack_loop = False
      for neighbour in legal_neighbours:
          if not self.taulukko[neighbour.y][neighbour.x].visited:

              x = neighbour.x
              y = neighbour.y

              stack.append(neighbour)
              self.taulukko[neighbour.y][neighbour.x].visited = True

              # check if we are at possible endpoint location and and this point to list.
              # TODO: add ending point.
              if (self.loppupiste.y == -1):
                # vasen tai oikea reuna
                if(self.loppupiste.x == x):
                  self.possible_endpoints.append((x, y))
                  # self.possible_endpoints.append(Piste(x, y))
              else:
                # ylä tai alareuna
                if(self.loppupiste.y == y):
                  self.possible_endpoints.append((x, y))
                  # self.possible_endpoints.append(Piste(x, y))


              if neighbour.direction == Direction.UP: 
                self.taulukko[y][x].wall_down = False
              elif neighbour.direction == Direction.DOWN: 
                self.taulukko[y-1][x].wall_down = False
              elif neighbour.direction == Direction.RIGHT: 
                self.taulukko[y][x-1].wall_right = False
              elif neighbour.direction == Direction.LEFT: 
                self.taulukko[y][x].wall_right = False

              # infomessages = []
              # infomessages.append(f"start: {self.maze.alkupiste}")
              # infomessages.append(f"end: {self.maze.loppupiste}")
              # infomessages.append(f"current: {current}")
              # infomessages.append(f"neighbour: {neighbour}")
              # infomessages.append(f"stack: {stack}")
              # self.maze.visualizer.visualize(self.maze, infomessages)
              # input("pressi enter.")

              continue_stack_loop = True

      if continue_stack_loop:
          continue

      stack.pop()

    return self
