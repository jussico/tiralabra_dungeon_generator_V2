import blessed 
from blessed.colorspace import RGB_256TABLE
import random
from visualizer.util import *

# https://blessed.readthedocs.io/_/downloads/en/latest/pdf/
# steelblue4 yms. 

from visualizer.base import Base

class ConsoleVisualizer(Base):

    def __init__(self):
        super().__init__()
        self.name = type(self).__name__
        self.logger = FileLogger()
        print(f"@init {self.name}")
        self.term = blessed.Terminal()
    
    def clear(self):
        print(self.term.normal + self.term.home + self.term.on_black + self.term.clear_eos)

    def visualize_it(self, cave, infomessages):
        print(f"@ConsoleVisualizer.visualize.it()")

        printable = self.render(cave, True)

        # clear screen after the maze so texts don't get messy.
        printable = printable + self.term.clear_eos

        for message in infomessages:
            printable = printable + f'{message}\n'

        printable = printable + '\n'

        print(self.term.home + self.term.on_black)

        print(printable, end='', flush=True)

    def render(self, cave, border = False):
        self.logger.logita("@render")

        taulukko = cave.taulukko
        leveys = cave.leveys
        korkeus = cave.korkeus

        printable = self.term.home

        # outer wall
        steel = self.term.lightsteelblue3('█')
        # inner wall
        rock = self.term.darkgoldenrod4('▓')
        # https://en.wikipedia.org/wiki/Block_Elements
        # ▓
        # ▒
        # ░
        empty = ' '
        starting_place = self.term.green('S')
        ending_place = self.term.orange('E')
        visited_char = self.term.blue('░')

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
                
                thing = empty
                other = empty

                if cell.visited:
                    thing = visited_char
                    other = visited_char

                if(cave.starting_point.pair() == (x,y)):
                    thing = starting_place
                if(cave.ending_point.pair() == (x,y)):
                    thing = ending_place

                new_upper_block = ''
                new_bottom_block = ''

                if cell.wall_right:
                    new_upper_block = thing + rock
                else:
                    new_upper_block = thing + other
                if cell.wall_bottom:
                    new_bottom_block = rock + rock
                else:
                    new_bottom_block = other + rock

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
