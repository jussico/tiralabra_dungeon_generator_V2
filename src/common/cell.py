

class Cell:

    def __init__(self):
        self.wall_down = True # TODO: rename -> bottom
        self.wall_right = True
        self.visited = False
        self.the_way = False

    def __str__(self):
        merkki = ' '
        if self.wall_down:
            merkki = '_'
        if self.wall_right:
            merkki = '|'
        if self.wall_down and self.wall_right:
            merkki = 'J'
        return merkki