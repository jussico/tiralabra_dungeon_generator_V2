import blessed 
from blessed.colorspace import RGB_256TABLE
import random
from common.util import *

# https://blessed.readthedocs.io/_/downloads/en/latest/pdf/
# steelblue4 yms. 

class ConsoleVisualizer:

    def __init__(self):
        self.name = type(self).__name__
        self.logger = FileLogger()
        print(f"@init {self.name}")
        self.term = blessed.Terminal()
        
    
    def clear(self):
        print(self.term.normal + self.term.home + self.term.on_black + self.term.clear_eos)

    def visualize(self, cave, infomessages):

        printable = self.render(cave.taulukko, cave.leveys, cave.korkeus, True)

        for message in infomessages:
            printable = printable + f'{message}\n'

        printable = printable + '\n'
        #printable = printable + self.term.clear_eos + '\n'

        # print(self.term.home + self.term.on_black + self.term.clear) # clear the screen
        print(self.term.home + self.term.on_black)

        print(printable, end='', flush=True)

    def render(self, taulukko, leveys, korkeus, border = False):
        self.logger.logita("@render")
        printable = self.term.home
        # printable = self.term.home + self.term.normal

        # outer wall
        steel = self.term.lightsteelblue3('█')
        # inner wall
        # rock = self.term.darkgoldenrod4('█')
        rock = self.term.darkgoldenrod4('▓')
        # https://en.wikipedia.org/wiki/Block_Elements
        # ▓
        # ▒
        # ░

        # possible top border
        if border:
            printable = (leveys * 2 + 2) * steel + '\n'

        for y in range(korkeus):
            row2 = ''
            
            # possible left border
            if border:  
                printable = printable + steel
                row2 = row2 + steel

            for x in range(leveys):
                cell = taulukko[y][x]

                new_upper_block = ''
                new_bottom_block = ''

                if cell.wall_right:
                    new_upper_block = ' ' + rock
                else:
                    new_upper_block = '  '
                if cell.wall_down:
                    new_bottom_block = rock + rock
                else:
                    new_bottom_block = ' ' + rock

                printable = printable + new_upper_block
                row2 = row2 + new_bottom_block

            # possible right border
            if border:  
                printable = printable + steel
                row2 = row2 + steel
            
            # finally add both generated rows
            printable = printable + '\n'
            printable = printable + row2 + '\n'

        # possible bottom border
        if border:
            printable = printable + (leveys * 2 + 2) * steel + '\n'
        
        printable = printable + '\n'
        printable += f'visualizer : {self.name}\n'

        # term.normal
        # term.center()
        # term.number_of_colors
        # blessed.color.COLOR_DISTANCE_ALGORITHMS
        # https://github.com/jquast/blessed/blob/master/docs/colors.rst

        return printable

    def __str__(self):
        return self.__class__.__name__
