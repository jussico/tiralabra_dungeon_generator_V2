import sys as realsys
import random
from generation.common_generation import *
from generation.dfs import *
from solving.dfs import *
from visualizer.ascii import *
from visualizer.console import *
from visualizer.console_compact import *
from visualizer.video import *
from visualizer.common_visualizer import *
from visualizer.dummy import *
import resource
import pickle


# creates some mazes and persists them so they can be used easily to test maze-solving algorithms.
def main():

    if realsys.argv[1] == 'test':
        print("testing loading #1.")
        filename = 'maze_persisted_01.data'
        with open(f'resources/{filename}', 'rb') as maze_file:
            maze = pickle.load(maze_file)
            # print some stuff
            print(maze)
            for row in maze.taulukko:
                print(row)

        print("testing loading #10.")
        filename = 'maze_persisted_10.data'
        with open(f'resources/{filename}', 'rb') as maze_file:
            maze = pickle.load(maze_file)
            # print some stuff
            print(maze)

        exit(0)

    # 1
    generate_and_persist(dummysys([
        'skip', 10, 10, 'dummy', 42, 'dfs'
        ]), 'maze_persisted_01.data')
    # 2
    generate_and_persist(dummysys([
        'skip', 20, 20, 'dummy', 43, 'dfs'
        ]), 'maze_persisted_02.data')
    # 3 still fits console
    generate_and_persist(dummysys([
        'skip', 25, 25, 'dummy', 44, 'dfs'
        ]), 'maze_persisted_03.data')
    # 4 small video size
    generate_and_persist(dummysys([
        'skip', 320/2, 256/2, 'dummy', 45, 'dfs'
        ]), 'maze_persisted_04.data')        
    # 5 pretty small video size
    generate_and_persist(dummysys([
        'skip', 640/2, 512/2, 'dummy', 46, 'dfs'
        ]), 'maze_persisted_05.data')                
    # 6 video size
    generate_and_persist(dummysys([
        'skip', 1024/2, 768/2, 'dummy', 47, 'dfs'
        ]), 'maze_persisted_06.data')                        
    # 7 video size FHD
    generate_and_persist(dummysys([
        'skip', 1920/2, 1080/2, 'dummy', 48, 'dfs'
        ]), 'maze_persisted_07.data')                                
    # 8 video size QHD
    generate_and_persist(dummysys([
        'skip', 2560/2, 1440/2, 'dummy', 49, 'dfs'
        ]), 'maze_persisted_08.data')                                        
    # 9 video size 4K
    generate_and_persist(dummysys([
        'skip', 3840/2, 2160/2, 'dummy', 50, 'dfs'
        ]), 'maze_persisted_09.data')                                                
    # 9 video size 8K
    generate_and_persist(dummysys([
        'skip', 7680/2, 4320/2, 'dummy', 51, 'dfs'
        ]), 'maze_persisted_10.data')                                                        

def generate_and_persist(sys, filename):

    main_term = blessed.Terminal()

    realsys.setrecursionlimit(10000) # TODO: enough?
    
    leveys, korkeus = int(sys.argv[1]), int(sys.argv[2])
    visualizer_name = sys.argv[3]
    random_seed = sys.argv[4]
    generation_name = sys.argv[5]
        
    if visualizer_name == Visualizer.ascii.name:
        visualizer = AsciiVisualizer()
    elif visualizer_name == Visualizer.consolemini.name:
        visualizer = ConsoleCompactVisualizer()
    elif visualizer_name == Visualizer.console.name:
        visualizer = ConsoleVisualizer()
    elif visualizer_name == Visualizer.video.name:
        visualizer = VideoVisualizer()
    elif visualizer_name == Visualizer.dummy.name:
        visualizer = DummyVisualizer()            
    else:
        # default to ascii
        sys.stderr.write(f"unknown visualizer: {visualizer_name}\n")
        visualizer = AsciiVisualizer()
        sys.stderr.write(f"defaulting to  visualizer: {visualizer}\n")

    # with -1 as random seed just dont set it.
    if random_seed != -1:
        random.seed(random_seed)

    # main_term.enter_fullscreen()

    generation = DfsGenerator(leveys, korkeus, visualizer)

    cave = generation.generate_maze()
    
    # persist
    with open(f'resources/{filename}', 'wb') as maze_persisted_file:
        pickle.dump(cave, maze_persisted_file)

    print("@ihan lopussa.")

class dummysys:
    def __init__(self, argv):
        self.argv = argv

if __name__ == "__main__":
    main()

