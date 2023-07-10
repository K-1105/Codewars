# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


try:
    from solution import decodeMorse as decode_morse
except ImportError:
    from solution import decode_morse

import codewars_test as test
import random

# preloaded dictionary - copied for tests security/integrity
MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

# used for generating random Morse codes
MORSE_KEYS = [k for k in MORSE_CODE.keys()]


@test.describe("Fixed tests")
def tests():
    @test.it("Should obtain correct decoding of Morse code from the description")
    def test_morse_hey_jude():
        test.assert_equals(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

    @test.it("Should obtain correct decoding of Morse code for basic examples")
    def test_morse_basic_examples():
        test.assert_equals(decode_morse('.-'), 'A')
        test.assert_equals(decode_morse('--...'), '7')
        test.assert_equals(decode_morse('...-..-'), '$')
        test.assert_equals(decode_morse('.'), 'E')
        test.assert_equals(decode_morse('..'), 'I')
        test.assert_equals(decode_morse('. .'), 'EE')
        test.assert_equals(decode_morse('.   .'), 'E E')
        test.assert_equals(decode_morse('...-..- ...-..- ...-..-'), '$$$')
        test.assert_equals(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
        test.assert_equals(decode_morse('.-... ---...   -..-. --...'), '&: /7')
        test.assert_equals(decode_morse('...---...'), 'SOS')
        test.assert_equals(decode_morse('... --- ...'), 'SOS')
        test.assert_equals(decode_morse('...   ---   ...'), 'S O S')

    @test.it("Should obtain correct decoding of Morse code for examples with extra spaces")
    def test_morse_basic_examples_with_extra_spaces():
        test.assert_equals(decode_morse(' . '), 'E')
        test.assert_equals(decode_morse('   .   . '), 'E E')

    @test.it(
        "Should obtain correct decoding of Morse code for a complex example, and should ignore leading and trailing whitespace")
    def test_morse_complex_example():
        test.assert_equals(decode_morse(
            '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
                           'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')


@test.describe("Random tests")
def tests():
    # reference solution
    def ref_decode(morse_code):
        return ' '.join(''.join(MORSE_CODE[c] for c in w.split(' ')) for w in morse_code.strip().split('   '))

    def get_random_morse(rand_len):
        '''
        - generates a random string, of approximate length rand_len, from the Morse characters that appear as keys in MORSE_CODE dictionary
        - randomly generates whitespace at the start and end of the string which should be ignored by user's solution as per Description
        - NEVER GENERATES consecutive '   ' within the randomly generated string
        ---
        - MORSE_KEYS is a list of the keys from MORSE_CODE
        '''
        rand_list = []

        # randomly generate whitespace, which should be ignored by user's solution as per Description
        # this will be added at the start and end of the final random Morse string
        rand_whitespace_length = random.randint(0, rand_len // 10)
        if rand_whitespace_length > 0:
            rand_whitespace_list = [' ' * rand_whitespace_length]

        while len(rand_list) < rand_len:
            # generate a NON-EMPTY list of Morse chars, i.e. of length AT LEAST 1, by randomly selecting a partial length of at least 1.
            # -> this ensures that we NEVER generate Morse strings with consecutive '   ' spaces in between Morse characters.
            rand_partial_length = random.randint(1, 2 + rand_len // 10)
            rand_partial_list = random.choices(MORSE_KEYS, k=rand_partial_length)
            rand_list.extend(rand_partial_list)
            # APPEND A SINGLE ' ' CHAR, which corresponds to adding a single **THREE SPACE STRING** in final string,
            # Why? -> because we will ' '.join() the list with ' ' so that the appended space ' ' chars will become '   ' in the resulting string.
            # This is because we don't want multiple occurences of triple-spaces between 2 NON-EMPTY words of Morse chars
            # i.e. "---         ..." <- we don't want this possibility.
            rand_list.append(' ')

        if rand_whitespace_length > 0:
            return ' '.join(rand_whitespace_list + rand_list + rand_whitespace_list)
        else:
            return ' '.join(rand_list)

    def rnd_tests(n_tests, min_len, max_len):
        msg = "Should obtain correct decoding of Morse code for {} random examples with {} <= approximate Morse code length <= {}"

        @test.it(msg.format(n_tests, min_len, max_len))
        def test_morse_random_examples():
            for _ in range(n_tests):
                rand_len = random.randint(min_len, max_len)
                rand_morse_code = get_random_morse(rand_len)
                exp = ref_decode(rand_morse_code)
                test.assert_equals(decode_morse(rand_morse_code), exp,
                                   "Returned solution incorrect for randomly generated Morse code {}".format(
                                       rand_morse_code))

    TESTS = [(10, 40, 80), (10, 80, 100), (10, 100, 200), (10, 200, 300), (10, 300, 400), (10, 400, 500)]
    for args in TESTS:
        rnd_tests(*args)