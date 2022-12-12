import sys
from generator.dfs import *
from visualizer.ascii import *
from visualizer.console import *
from visualizer.console_compact import *
from visualizer.video import *

def main():

    main_term = blessed.Terminal()

    print(f'sys.getrecursionlimit(): {sys.getrecursionlimit()}')
    sys.setrecursionlimit(10000) # TODO: enough?
    print(f'sys.getrecursionlimit(): {sys.getrecursionlimit()}')

    print(f'sys.argv: {sys.argv}')
    print(f'len(sys.argv): {len(sys.argv)}')

    if len(sys.argv) > 3:
        leveys, korkeus = int(sys.argv[1]), int(sys.argv[2])
        visualizer_name = sys.argv[3]
        if visualizer_name == "ascii":
            visualizer = AsciiVisualizer()
        elif visualizer_name == "consolemini":
            visualizer = ConsoleCompactVisualizer()
        elif visualizer_name == "console":
            visualizer = ConsoleVisualizer()
        elif visualizer_name == "video":
            visualizer = VideoVisualizer()
        else:
            # default to ascii
            sys.stderr.write(f"unknown visualizer: {visualizer_name}\n")
            visualizer = AsciiVisualizer()
            sys.stderr.write(f"defaulting to  visualizer: {visualizer}\n")
    else:
        print('ei sopivia argumentteja - käytetään oletusargumentteja.')
        # leveys, korkeus = 10, 10
        leveys, korkeus = 20, 20
        visualizer = AsciiVisualizer()

    print(f'leveys: {leveys} korkeus: {korkeus} visualizer: {visualizer}')


    input("Press Enter to start...")

    main_term.enter_fullscreen()

    # TODO
    # from queue import LifoQueue
    # pino = LifoQueue(maxsize=leveys * korkeus)

    maze = DfsGenerator(leveys, korkeus, visualizer)


    input("Finished. Press Enter to end.")

    main_term.exit_fullscreen()

    # TODO: pathfinder algorithm
    # visualizer.visualize(maze)

    print("@ihan lopussa.")

if __name__ == "__main__":
    main()
