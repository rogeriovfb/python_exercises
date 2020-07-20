"""
Our fleet managed to get one of the enemy's top-secret codes from the remains of its fallen ship.
The codes were immediately sent over to our code-breaking base over at Bleckley Park ;) for analysis.
The team found that each code contains 25 numbers with one missing.
The missing number corresponds to a letter in the English alphabet.
Your job is to find a more efficient Method of decrypting the messages by digitizing the process.

Write a function that takes a list, detects the missing number (in the list), and returns its corresponding letter.

Examples
decrypt(24, 12, 2, ..., 25) ➞ "N"
# The missing number is 14.

decrypt(24, 12, 2, ..., 25) ➞ "O"
# The missing number is 15.

decrypt(24, 12, 2, ..., 25) ➞ "P"
# The missing number is 16.

Notes
The list will only contain positive integers from 1 to 26 with one missing.
There will be no duplicate numbers.
Return the capital letter.

"""
from string import ascii_uppercase


def decrypt(entrada: list):
    return [ascii_uppercase[num-1] for num in range(1, 27) if num not in entrada][0]


assert decrypt([21, 2, 5, 25, 7, 20, 15, 3, 6, 9, 16, 19, 1, 4, 11, 22, 10, 13, 12, 18, 24, 17, 23, 14, 26]) == "H"
