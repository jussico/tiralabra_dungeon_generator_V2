
class Base:

    def __init__(self):
        self.cleared = False

    def visualize(self, maze, infomessages):
        if maze.solved or maze.framedrop == 0 or maze.frame % maze.framedrop == 0:
            if not self.cleared: 
                self.clear()
                self.cleared = True
            self.visualize_it(maze, infomessages)
            if(maze.interactive): input("press enter to continue.")

    # @abstract
    def clear(self):
        pass

    def reset(self):
        self.cleared = False

    def __str__(self):
        return self.__class__.__name__
