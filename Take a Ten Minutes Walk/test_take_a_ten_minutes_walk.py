import unittest
from take_a_ten_minutes_walk import is_valid_walk


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True, 'should return True');
        self.assertEqual(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False, 'should return False');
        self.assertEqual(is_valid_walk(['w']), False, 'should return False');
        self.assertEqual(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), False, 'should return False');
