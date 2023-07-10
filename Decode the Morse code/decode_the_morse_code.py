# n this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
#
# NOTE: Extra spaces before or after the code have no meaning and should be ignored.
#
# In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.
#
# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.
#
# For example:
#
# decode_morse('.... . -.--   .--- ..- -.. .')
# #should return "HEY JUDE"
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

MORSE_CODE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
    }

def decode_morse(morse_code):
    # "NOTE: Extra spaces before or after the code have no meaning and should be ignored." so get rif of them...
    morse_code = morse_code.strip()
    # make a list or the morse code words
    mc_words = morse_code.split("  ")
    # make a list of letters in the list of words
    mc_words_to_letters = [word.split(" ") for word in mc_words]
    # convert the letters if they are not a just a blank from the words separating, if they are return a space, do this for every letter in the letters lists in the words list
    decoded_mc_letters = [MORSE_CODE[letter] if letter != "" else " " for word in mc_words_to_letters for letter in word]
    # join all the aplphas back togther as as string
    decoded_message = ''.join(decoded_mc_letters)
    return decoded_message




