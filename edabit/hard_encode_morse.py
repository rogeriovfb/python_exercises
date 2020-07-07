"""
Create a function that takes a string as an argument and return a non-encoded, encrypted string.
Examples
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

Notes
Input value can be lower or upper case.
Input string can have digits.
Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
"""
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def encode_morse(word):
    encoded = ''
    for letter in word:
        encoded = encoded + char_to_dots[letter.upper()] + ' '
    return encoded[:-1]


assert encode_morse("EDABBIT CHALLENGE") == ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
assert encode_morse("HELP ME !") == ".... . .-.. .--.   -- .   -.-.--"
