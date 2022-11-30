

class Cell:

    def __init__(self):
        self.wall_down = True # TODO: rename -> bottom
        self.wall_right = True
        self.visited = False
        self.the_way = False

    def __str__(self):
        stringi = f'wall_bottom: {self.wall_down} \n'
        stringi = stringi + f'wall_right: {self.wall_right} \n'
        stringi = stringi + f'visited: {self.visited} \n'
        return stringi