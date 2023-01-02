import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import unittest
from solving.dfs import *
from generation.dfs import *
from visualizer.dummy import *
from visualizer.console import *
from main import Main
from visualizer.ascii import *
from generation.hardcoded import *

class TestDfs(unittest.TestCase):

    def test_dfs(self):
        # create maze
        solving = Dfs()
        generation = DfsGenerator(32, 16, DummyVisualizer(), False, 10, "dfs", 42)

        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertTrue(route) # not empty

    def test_dfs_with_empty_maze(self):
        # create maze
        solving = Dfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_A.name, DummyVisualizer(), False, 10, "dfs", 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertTrue(route) # not empty

    def test_dfs_with_empty_maze_B(self):
        # create maze
        solving = Dfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_B.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertTrue(route) # not empty

    def test_dfs_with_empty_maze_C(self):
        # create maze
        solving = Dfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_C.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertTrue(route) # not empty

    def test_dfs_with_empty_maze_D(self):
        # create maze
        solving = Dfs()
        generation = HardCodedGenerator(HardCodedMaze.empty_D.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertTrue(route) # not empty

    def test_dfs_with_fail_A(self):
        # create maze
        solving = Dfs()
        generation = HardCodedGenerator(HardCodedMaze.fail_A.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, False)
        self.assertIsNone(route)


# testing test class
if __name__ == "__main__":
    visualizer = ConsoleVisualizer()
    # visualizer = DummyVisualizer()

    # DFS GENERATED
    # generation = DfsGenerator(32, 16, visualizer, False, 10, "dfs", 42)
    # maze = generation.generate_maze()

    # HARDCODED
    # generation = HardCodedGenerator(HardCodedMaze.empty_A.name, DummyVisualizer(), False, 10, "dfs", 42)
    # maze = generation.generate_maze()

    solving = Dfs()
    generation = HardCodedGenerator(HardCodedMaze.fail_A.name, ConsoleVisualizer(), False, 10, solving.__class__.__name__, 42)
    maze = generation.generate_maze()

    # print(f"maze: {maze.infostring()}")
    # viz = AsciiVisualizer()
    # viz.visualize(maze, ["jyy"])

    print(f"maze: {maze.infostring()}")
    viz = ConsoleVisualizer()
    viz.visualize(maze, ["jyy"])    
    input()

    solving = Dfs()
    solved, route = solving.solve(maze)
    print(f"solved: {solved}")
    print(f"route: {route}")


