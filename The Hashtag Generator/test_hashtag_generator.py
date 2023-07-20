import unittest
from hashtag_generator import generate_hashtag


class MyTestCase(unittest.TestCase):
    def test_correct_hashtag_fixed(self):
        self.assertEqual(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
        self.assertEqual(generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.')
        self.assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
        self.assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice',
                         'Should capitalize first letters of words.')
        self.assertEqual(generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice',
                         'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')
        self.assertEqual(generate_hashtag('c i n'), '#CIN',
                         'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')
        self.assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice',
                         'Should deal with unnecessary middle spaces.')

    # "Should return False if the input is empty, or result is longer than 140 chars")
    def test_false_hashtag_fixed(self):
        self.assertEqual(generate_hashtag(''), False, 'Expected an empty string to return False')
        self.assertEqual(generate_hashtag(
            'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
                         False, 'Should return False if the final string is longer than 140 chars.')


if __name__ == '__main__':
    unittest.main()
