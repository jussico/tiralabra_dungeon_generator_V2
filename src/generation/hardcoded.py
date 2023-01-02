
from common.cell import *
from common.point import *
from common.maze import *
from enum import Enum

# hardcoded mazes used for testing.
class HardCodedMaze(Enum):
  empty_A = 1 # (0,0) (max, max)
  empty_B = 2 # (0,0) (max, 0)
  empty_C = 3 # (0,0) (0, max)
  empty_D = 4 # (0,0) (max/2, max/2)
  fail_A = 5 # exit blocked

class HardCodedGenerator(Maze):

  def __init__(self, maze_name, visualizer, interactive, framedrop, solving_name, random_seed):
    self.maze_name = maze_name
    
    width, height = 10, 10
    if maze_name in [HardCodedMaze.empty_A.name, HardCodedMaze.empty_B.name, HardCodedMaze.empty_C.name, HardCodedMaze.empty_D.name, HardCodedMaze.fail_A.name ]:
      width = 12
      height = 8
    else:
      print(f"maze name not found: {maze_name}")
      exit(0)

    super().__init__(width, height, visualizer, interactive, framedrop, solving_name, random_seed)

  def generate_maze(self):

    # break down all the walls
    for y in range(self.korkeus):
        for x in range(self.leveys):
            self.taulukko[y][x].wall_bottom = False
            self.taulukko[y][x].wall_right = False

    if self.maze_name == HardCodedMaze.empty_A.name:
      self.starting_point = Point(0,0)
      self.ending_point = Point(self.leveys - 1, self.korkeus - 1)
    elif self.maze_name == HardCodedMaze.empty_B.name:
      self.starting_point = Point(0,0)
      self.ending_point = Point(self.leveys - 1, 0)
    elif self.maze_name == HardCodedMaze.empty_C.name:
      self.starting_point = Point(0,0)
      self.ending_point = Point(0, self.korkeus - 1)
    elif self.maze_name == HardCodedMaze.empty_D.name:
      self.starting_point = Point(0,0)
      self.ending_point = Point(self.leveys / 2, self.korkeus / 2)
    elif self.maze_name == HardCodedMaze.fail_A.name:
      self.starting_point = Point(0,0)
      halfway_x = int(self.leveys / 2)
      halfway_y = int(self.korkeus / 2)
      self.ending_point = Point(halfway_x + 1, halfway_y + 1)      
      self.taulukko[halfway_y][halfway_x].wall_bottom = True
      self.taulukko[halfway_y][halfway_x].wall_right = True
      self.taulukko[halfway_y+1][halfway_x].wall_bottom = True
      self.taulukko[halfway_y+1][halfway_x].wall_right = True
      self.taulukko[halfway_y+2][halfway_x].wall_bottom = True
      self.taulukko[halfway_y+2][halfway_x].wall_right = True      

      self.taulukko[halfway_y][halfway_x+1].wall_bottom = True
      self.taulukko[halfway_y][halfway_x+1].wall_right = True
      self.taulukko[halfway_y+2][halfway_x+1].wall_bottom = True
      self.taulukko[halfway_y+2][halfway_x+1].wall_right = True      

      self.taulukko[halfway_y][halfway_x+2].wall_bottom = True
      self.taulukko[halfway_y][halfway_x+2].wall_right = True
      self.taulukko[halfway_y+1][halfway_x+2].wall_bottom = True
      self.taulukko[halfway_y+1][halfway_x+2].wall_right = True
      self.taulukko[halfway_y+2][halfway_x+2].wall_bottom = True
      self.taulukko[halfway_y+2][halfway_x+2].wall_right = True      

    return self
        

    
    


