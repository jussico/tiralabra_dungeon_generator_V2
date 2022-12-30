import random
from common.util import *
import time
from datetime import datetime
import os

from visualizer.base import Base

class VideoVisualizer(Base):

    def __init__(self):
        super().__init__()
        self.initialized = False

    def video_init(self, maze):
        if not self.initialized:
            self.initialized = True
            self.name = type(self).__name__
            print(f"@init {self.name}")

            date_time = datetime.fromtimestamp(time.time())
            # convert timestamp to string in dd-mm-yyyy HH:MM:SS
            self.folder_name = \
                f'video_images/video-@date-{maze.solving_name}' \
                    + date_time.strftime("%Y-%m-%d_time_%H_%M_%S_%f")
            self.create_image_folder()
            self.frame = 1

    def create_image_folder(self):
        print(f"creating folder for video: {self.folder_name}")
        os.makedirs(self.folder_name)
        os.chdir(self.folder_name)
        print(f"directory now: {format(os.getcwd())}")

    def create_file_header(self, cave, border):
        # https://en.wikipedia.org/wiki/Netpbm#File_formats
        printable = "P2\n"
        printable = printable + "# kommentti\n"
        image_widht = 2 * cave.leveys 
        image_heigth = 2 * cave.korkeus
        if border:
            image_widht = image_widht + 2
            image_heigth = image_heigth + 2
        printable = printable + f"{image_widht} {image_heigth}\n"
        printable = printable + "10\n" # gray scale
        return printable

    def visualize_it(self, cave, infomessages):

        self.video_init(cave)

        border = True

        printable = self.create_file_header(cave, border)

        # printable = printable + self.render(cave.taulukko, cave.leveys, cave.korkeus, border)
        printable = printable + self.render(cave, border)

        # TODO: maybe add infotexts to image?
        # for message in infomessages:
        #     printable = printable + f'{message}\n'

        # printable = printable + '\n'
        # #printable = printable + self.term.clear_eos + '\n'

        # # print(self.term.home + self.term.on_black + self.term.clear) # clear the screen
        # print(self.term.home + self.term.on_black)

        # print(printable, end='', flush=True)

        # print(printable)
        new_file_name = f"frame_{self.frame:07d}.pbm"
        new_file = open(new_file_name, "w")
        new_file.write(printable)
        new_file.close()

        print(f"frame {self.frame} written to file {new_file_name}.")
        self.frame = self.frame + 1

    # def render(self, taulukko, leveys, korkeus, border = False):
    def render(self, cave, border = False):

        taulukko = cave.taulukko
        leveys = cave.leveys
        korkeus = cave.korkeus

        steel = '7 '
        rock = '5 '
        # empty = '  '
        empty = '0 '
        starting_place = '4 '
        ending_place = '9 '
        visited_char = '2 '

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

                if(cave.alkupiste.pair() == (x,y)):
                    thing = starting_place
                if(cave.loppupiste.pair() == (x,y)):
                    thing = ending_place                

                new_upper_block = ''
                new_bottom_block = ''

                if cell.wall_right:
                    new_upper_block = thing + rock
                else:
                    new_upper_block = thing + other
                if cell.wall_down:
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

        return printable
