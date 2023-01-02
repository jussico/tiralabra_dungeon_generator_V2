
from visualizer.base import Base

class AsciiVisualizer(Base):

  # TODO: maybe
  # https://en.wikipedia.org/wiki/Box_Drawing

  def clear(self):
      pass

  def visualize_it(self, maze, infomessages):

    # TODO: nicer characters(?)    
    top_border  = "_"
    left_border = '|'
    reuna = '█'
    
    # top border
    printable = (maze.leveys * 2 + 1) * top_border + '\n'

    for y in range(maze.korkeus):
      # left border
      printable = printable + left_border
      for x in range(maze.leveys):
        if maze.taulukko[y][x].wall_down:
          printable = printable + '_'
        else:
          printable = printable + ' '
        if maze.taulukko[y][x].wall_right:
          printable = printable + '|'
        else:
          printable = printable + '.'
      # right border
      printable = printable + '\n'
    # bottom border

    # infotexts below maze
    printable = printable + '\n'    
    printable = printable + f'visualizer : {self}\n'
    printable = printable + f'starting_point : {maze.starting_point}\n'
    printable = printable + f'ending_point : {maze.ending_point}\n'
    for message in infomessages:
      printable = printable + f'{message}\n'

    print(printable)
