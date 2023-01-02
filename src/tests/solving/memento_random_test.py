import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from solving.memento_random import *
from generation.dfs import *
from visualizer.dummy import *
from main import Main
from generation.hardcoded import *

class TestMementoRandom(unittest.TestCase):

    def test_memento_random(self):
        # create maze
        solving = MementoRandom()
        generation = DfsGenerator(16, 8, DummyVisualizer(), False, 0, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertIsNone(route)

    def test_memento_random_with_empty_maze_B(self):
        # create maze
        solving = MementoRandom()
        generation = HardCodedGenerator(HardCodedMaze.empty_B.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertIsNone(route)

    def test_memento_random_with_empty_maze_C(self):
        # create maze
        solving = MementoRandom()
        generation = HardCodedGenerator(HardCodedMaze.empty_C.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertIsNone(route)

    def test_memento_random_with_empty_maze_D(self):
        # create maze
        solving = MementoRandom()
        generation = HardCodedGenerator(HardCodedMaze.empty_D.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertIsNone(route)

    def test_memento_random_with_fail_A(self):
        # create maze
        solving = MementoRandom()
        generation = HardCodedGenerator(HardCodedMaze.fail_A.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, False)
        self.assertIsNone(route)


