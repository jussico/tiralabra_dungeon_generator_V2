import unittest
from generator.cave_generator import CaveGenerator

class TestCaveGenerator(unittest.TestCase):
    def setUp(self):
        print("@setUp")
        self.gen = CaveGenerator()

    def test_dummy(self):
        print("@test_dummy")
        self.assertEqual(True, True)

# if __name__ == '__main__':
#     unittest.main()
