import unittest

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from main import Main

class TestDfs(unittest.TestCase):
    def setUp(self):
        print("@setUp")
        self.main_class = Main()

    def test_dfs_randomized(self):
        print("@test_dfs_randomized")
        self.main_class.main(['main.py', \
            32, 16, 'dummy', 42, 'dfs', 'dfs_randomized', 'silent', 1000])        
        self.assertEqual(True, True)
