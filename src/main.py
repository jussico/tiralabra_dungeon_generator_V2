import sys
import random
from generation.common_generation import *
from solving.common_solving import *
from generation.dfs import *
from solving.bfs import *
from solving.dfs_randomized import *
from solving.bfs_randomized import *
from solving.dijkstra import *
from solving.astar import *
from solving.astar_jump_point import *
from solving.memento_random import *
# from solving.jump_point import *
from solving.wall_follower import *
from visualizer.ascii import *
from visualizer.console import *
from visualizer.console_compact import *
from visualizer.video import *
from visualizer.common_visualizer import *
from visualizer.dummy import *

# argumentit:
# leveys korkeus visualizer-name randomseed maze-generation-algorithm-name 
# (jatkuu) maze-solving-algorithm-name
# esim:
# python src/main.py 20 20 console 666 dfs dfs silent 10
class Main:
    def main(self, arguments):

        main_term = blessed.Terminal()

        print('@main.py main() method beginning.')
        print(f'got arguments: {arguments}')

        if len(arguments) > 8:
            leveys, korkeus = int(arguments[1]), int(arguments[2])
            visualizer_name = arguments[3]
            random_seed = arguments[4]
            generation_name = arguments[5]
            solving_name = arguments[6]
            silent = arguments[7]
            framedrop = arguments[8]
            
            if visualizer_name == Visualizer.ascii.name:
                visualizer = AsciiVisualizer()
                print("TODO: not updated")
                exit(0)
            elif visualizer_name == Visualizer.consolemini.name:
                visualizer = ConsoleCompactVisualizer()
                print("TODO: not updated")
                exit(0)            
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

            if silent == "silent":
                interactive = False
            else:
                interactive = True

            # with -1 as random seed just dont set it.
            if random_seed != -1:
                random.seed(random_seed)
                
            if generation_name == Generation.dfs.name:
                generation = DfsGenerator(leveys, korkeus, visualizer, interactive, framedrop, solving_name)
            # else if generation_name == Generation.bfs.name:

            if solving_name == Solving.dfs.name:
                solving = Dfs()
            elif solving_name == Solving.bfs.name:
                solving = Bfs()
            elif solving_name == Solving.dfs_randomized.name:
                solving = DfsRandomized()            
            elif solving_name == Solving.bfs_randomized.name:
                solving = BfsRandomized()            
            elif solving_name == Solving.dijkstra.name:
                solving = Dijkstra()
            elif solving_name == Solving.astar.name:
                solving = Astar()
            elif solving_name == Solving.astar_jump_point.name:
                solving = AstarJumpPoint()            
            elif solving_name == Solving.memento_random.name:
                solving = MementoRandom()
            elif solving_name == Solving.wall_follower.name:
                solving = WallFollower()

        else:
            print('no suitable arguments - using default arguments.')
            # leveys, korkeus = 10, 10
            leveys, korkeus = 20, 20
            visualizer = AsciiVisualizer()
            solving = Dfs()
            random_seed = 7
            interactive = True

        # print(f'leveys: {leveys} korkeus: {korkeus} visualizer: {visualizer}')
        # print(f'random_seed: {random_seed}')
        print('using classes {generation, solving, visualizer}: ' + f'{generation}, {solving}, {visualizer}')

        if interactive: input("Press Enter to start...")
        
        main_term.enter_fullscreen()

        # TODO
        # from queue import LifoQueue
        # pino = LifoQueue(maxsize=leveys * korkeus)

        if interactive: input("press enter to generate maze.")

        # generation = DfsGenerator(leveys, korkeus, visualizer, interactive)

        maze = generation.generate_maze()

        print("maze generated.")
        if interactive: input("press enter to solve maze.")

        solving.solve(maze)

        print("maze solving finished.")
        if interactive: input("press enter to end.")

        main_term.exit_fullscreen()

        print('@main.py main() method dead-beat, right at the end.\n')

if __name__ == "__main__":
    main_class = Main()
    main_class.main(sys.argv)
