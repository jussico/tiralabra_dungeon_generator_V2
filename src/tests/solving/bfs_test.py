import os
import sys
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import unittest
from solving.bfs import *
from generation.dfs import *
from visualizer.dummy import *
from main import Main
from generation.hardcoded import *

class TestBfs(unittest.TestCase):

    def test_bfs(self):
        # create maze
        solving = Bfs()
        generation = DfsGenerator(32, 16, DummyVisualizer(), False, 0, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertIsNotNone(route) # not empty

        # self.main_class.main(['main.py', \
        #     32, 16, 'dummy', 42, 'dfs', 'astar', 'silent', 1000])        

        # self.assertEqual(True, True)

    def test_bfs_with_empty_maze(self):
        # create maze
        solving = Bfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_A.name, DummyVisualizer(), False, 10, "bfs", 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.leveys + maze.korkeus - 1)

    def test_bfs_with_empty_maze_B(self):
        # create maze
        solving = Bfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_B.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.leveys)

    def test_bfs_with_empty_maze_C(self):
        # create maze
        solving = Bfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_C.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.korkeus)

    def test_bfs_with_empty_maze_D(self):
        # create maze
        solving = Bfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_D.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.leveys / 2 + maze.korkeus / 2 + 1)

    def test_bfs_with_fail_A(self):
        # create maze
        solving = Bfs()
        generation = HardCodedGenerator(HardCodedMaze.fail_A.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, False)
        self.assertIsNone(route)



# testing test class
if __name__ == "__main__":
    # visualizer = ConsoleVisualizer()
    # visualizer = DummyVisualizer()

    # DFS GENERATED
    # generation = DfsGenerator(32, 16, visualizer, False, 10, "dfs", 42)
    # maze = generation.generate_maze()

    # HARDCODED
    generation = HardCodedGenerator(HardCodedMaze.empty_A.name, DummyVisualizer(), False, 10, "bfs", 42)
    maze = generation.generate_maze()

    # print(f"maze: {maze.infostring()}")
    # viz = AsciiVisualizer()
    # viz.visualize(maze, ["jyy"])

    # print(f"maze: {maze.infostring()}")
    # viz = ConsoleVisualizer()
    # viz.visualize(maze, ["jyy"])    

    solving = Bfs()
    solved, route = solving.solve(maze)
    print(f"solved: {solved}")
    print(f"route: {route}")
