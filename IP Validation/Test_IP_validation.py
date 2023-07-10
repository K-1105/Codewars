import unittest
from IP_Validation import is_valid_IP

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_valid_IP(''),                False)
        self.assertEqual(is_valid_IP('12.255.56.1'),     True)
        self.assertEqual(is_valid_IP('abc.def.ghi.jkl'), False)
        self.assertEqual(is_valid_IP('123.456.789.0'),   False)
        self.assertEqual(is_valid_IP('12.34.56'),        False)
        self.assertEqual(is_valid_IP('12.34.56 .1'),     False)
        self.assertEqual(is_valid_IP('12.34.56.-1'),     False)
        self.assertEqual(is_valid_IP('123.045.067.089'), False)
        self.assertEqual(is_valid_IP('127.1.1.0'),        True)
        self.assertEqual(is_valid_IP('0.0.0.0'),          True)
        self.assertEqual(is_valid_IP('0.34.82.53'),       True)
        self.assertEqual(is_valid_IP('192.168.1.300'),   False)
