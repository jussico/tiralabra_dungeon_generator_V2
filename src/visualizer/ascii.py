
class AsciiVisualizer:

  # TODO: maybe
  # https://en.wikipedia.org/wiki/Box_Drawing

  def clear(self):
      pass

  # def visualize(self, maze, location_x, location_y, direction):
  def visualize(self, maze, infomessages):
    
    # ylhäälle ja alas täytyy piirtää visuaalisuuden vuoksi ylimääräiset rivit 
    # koska tietorakenteessa seinät ovat vain alhaalla ja oikealla.
    top_border  = "_"
    left_border = '|'
    reuna = '█'
    
    # piirrä yläreuna
    printable = (maze.leveys * 2 + 1) * top_border + '\n'

    for y in range(maze.korkeus):
      # piirrä vasen reuna
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
      # mahdollinen oikea reuna olisi tässä
      printable = printable + '\n'
    # mahdollinen alareuna olisi tässä

    # infotexts below
    printable = printable + '\n'    
    printable = printable + f'visualizer : {self}\n'
    printable = printable + f'alkupiste : {maze.alkupiste}\n'
    for message in infomessages:
      printable = printable + f'{message}\n'

    print(printable)

  def __str__(self):
    return self.__class__.__name__
