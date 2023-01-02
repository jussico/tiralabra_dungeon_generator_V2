
from common.cell import *
from common.point import *
from common.maze import *

class DfsGenerator(Maze):

  def generate_with_endpoint(self, x, y, direction = None):

    self.generate(x, y, direction = None)

    # select endpoint from list of possible endpoints
    random_end_point_pair = self.possible_endpoints[random.randrange(0,len(self.possible_endpoints))]
    self.ending_point = Point(random_end_point_pair[0], random_end_point_pair[1])

    # final draw after maze fully generated
    infomessages = [ "maze generation finished." ]

    self.visualizer.visualize(self, infomessages)

    return self

  # generates the self.taulukko with depth-first algorithm
  def generate(self, x, y, direction = None):
    
    infomessages = []
    infomessages.append(f'x: {x} y: {y} direction: {direction}')
    self.visualizer.visualize(self, infomessages)

    stack = []
    stack.append(self.starting_point)
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
              if (self.ending_point.y == -1):
                # vasen tai oikea reuna
                if(self.ending_point.x == x):
                  self.possible_endpoints.append((x, y))
              else:
                # ylä tai alareuna
                if(self.ending_point.y == y):
                  self.possible_endpoints.append((x, y))

              if neighbour.direction == Direction.UP: 
                self.taulukko[y][x].wall_bottom = False
              elif neighbour.direction == Direction.DOWN: 
                self.taulukko[y-1][x].wall_bottom = False
              elif neighbour.direction == Direction.RIGHT: 
                self.taulukko[y][x-1].wall_right = False
              elif neighbour.direction == Direction.LEFT: 
                self.taulukko[y][x].wall_right = False

              continue_stack_loop = True

      if continue_stack_loop:
          continue

      stack.pop()

    return self
