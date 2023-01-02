import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import unittest
from solving.astar import *
from generation.dfs import *
from visualizer.dummy import *
from main import Main
from generation.hardcoded import *

class TestAstar(unittest.TestCase):

    def test_astar(self):
        # create maze
        solving = Astar()
        generation = DfsGenerator(32, 16, DummyVisualizer(), False, 1000, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertTrue(route) # not empty

    def test_astar_with_empty_maze_A(self):
        # create maze
        solving = Astar()
        generation = HardCodedGenerator(HardCodedMaze.empty_A.name, DummyVisualizer(), False, 10, "astar", 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.leveys + maze.korkeus - 1)

    def test_astar_with_empty_maze_B(self):
        # create maze
        solving = Astar()
        generation = HardCodedGenerator(HardCodedMaze.empty_B.name, DummyVisualizer(), False, 10, "astar", 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.leveys)

    def test_astar_with_empty_maze_C(self):
        # create maze
        solving = Astar()
        generation = HardCodedGenerator(HardCodedMaze.empty_C.name, DummyVisualizer(), False, 10, "astar", 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.korkeus)

    def test_astar_with_empty_maze_D(self):
        # create maze
        solving = Astar()
        generation = HardCodedGenerator(HardCodedMaze.empty_D.name, DummyVisualizer(), False, 10, "astar", 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, True)
        self.assertEqual(len(route), maze.leveys /2 + maze.korkeus /2 + 1)

    def test_astar_with_fail_A(self):
        # create maze
        solving = Astar()
        generation = HardCodedGenerator(HardCodedMaze.fail_A.name, DummyVisualizer(), False, 10, solving.__class__.__name__, 42)
        maze = generation.generate_maze()

        # solve maze
        solved, route = solving.solve(maze)

        # check result
        self.assertEqual(solved, False)
        self.assertIsNone(route)
