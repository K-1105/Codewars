import unittest
from build_tower import tower_builder


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(tower_builder(1), ['*', ])
        self.assertEqual(tower_builder(2), [' * ', '***'])
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])
