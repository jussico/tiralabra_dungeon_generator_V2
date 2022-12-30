import random
from common.util import *
import time
from datetime import datetime
import os

from visualizer.base import Base
from visualizer.black_and_white_video import *

class VideoVisualizer(BlackAndWhiteVideoVisualizer):

    def __init__(self):
        super().__init__()

    def video_init(self, maze):
        if not self.initialized:
            super().video_init(maze)
            # color format values
            self.steel = '7 7 7   '
            self.rock = '5 5 5   '
            # empty = '  '
            self.empty = '0 0 0   '
            self.starting_place = '9 0 0   '
            self.ending_place = '0 9 0   '
            self.visited_char = '2 2 2   '            

    def create_file_header(self, cave, border):
        # https://en.wikipedia.org/wiki/Netpbm#File_formats
        printable = "P3\n"
        printable = printable + "# kommentti\n"
        image_widht = 2 * cave.leveys 
        image_heigth = 2 * cave.korkeus
        if border:
            image_widht = image_widht + 2
            image_heigth = image_heigth + 2
        printable = printable + f"{image_widht} {image_heigth}\n"
        printable = printable + "9\n" # max value for each color
        return printable
