import unittest
from human_time import format_duration


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")


if __name__ == '__main__':
    unittest.main()
