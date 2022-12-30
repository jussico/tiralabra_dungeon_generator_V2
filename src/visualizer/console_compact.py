import blessed 
from blessed.colorspace import RGB_256TABLE
import random
from common.util import *

# https://blessed.readthedocs.io/_/downloads/en/latest/pdf/
# steelblue4 yms. 

from visualizer.base import Base

class ConsoleCompactVisualizer(Base):

    def __init__(self):
        super().__init__()
        self.logger = FileLogger()
        print(f"@init {self}")
        self.term = blessed.Terminal()

    def clear(self):
        print(self.term.normal + self.term.home + self.term.on_black + self.term.clear_eos)

    def visualize_it(self, cave, infomessages):
        printable = self.render(cave.taulukko, cave.leveys, cave.korkeus, True)
        
        for message in infomessages:
            printable = printable + f'{message}\n'

        printable = printable + '\n'
        # printable = printable + self.term.clear_eos + '\n'

        # clear the screen
        # print(self.term.home + self.term.on_black + self.term.clear) 
        print(self.term.home + self.term.on_black) 
        
        # print the maze and infomessages
        print(printable, end='', flush=True)

    def render(self, taulukko, leveys, korkeus, border = False):
        self.logger.logita("@render")
        
        # string begins like this
        printable = self.term.home + self.term.normal

        reuna = self.term.lightsteelblue3('█')

        # possible top border
        if border:
            printable = (leveys * 2 + 2) * reuna + '\n'
        
        for y in range(korkeus):

            # possible left border
            if border:  
                printable = printable + reuna

            for x in range(leveys):
                cell = taulukko[y][x]
                if cell.wall_down:
                    printable = printable + self.term.darkgoldenrod4('_')
                else:
                    printable = printable + ' '
                if cell.wall_right:
                    printable = printable + self.term.darkgoldenrod4('|')
                else:
                    printable = printable + self.term.darkgoldenrod4('.')

            # possible right border
            if border:  
                printable = printable + reuna

            printable = printable + '\n'
        
        # possible bottom border
        if border:
            printable = printable + (leveys * 2 + 2) * reuna + '\n'

        # infotexts below
        printable = printable + '\n'
        printable += f'visualizer : {self}\n'

        # term.normal
        # term.center()
        # term.number_of_colors
        # blessed.color.COLOR_DISTANCE_ALGORITHMS
        # https://github.com/jquast/blessed/blob/master/docs/colors.rst


        return printable
