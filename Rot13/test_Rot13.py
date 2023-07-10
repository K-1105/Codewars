import unittest
from Rot13 import rot13


class TestRot13(unittest.TestCase):

    def test_rot13_fixed_strings(self):
        self.assertEqual(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        self.assertEqual(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%',
                           'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')


