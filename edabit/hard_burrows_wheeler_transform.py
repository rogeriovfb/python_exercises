"""
Burrows-Wheeler transform (BWT) is an algorithm which is used in data compression.
Given a string text, BWT of text is a modified version of the string with same length as text.
It can then be used to efficiently find substrings of text (which won't be covered here).
We will just find the BWT of text.

    Build Burrows-Wheeler-Matrix (BWM) containing all rotations of text.
    Sort BWM lexicographically ($ < a < b < ... < z).
    BWT is the last coloumn of BWM and gets returned.

# Example with text = "banana$"

# BWM (all rotations of text):
banana$
anana$b
nana$ba
ana$ban
na$bana
a$banan
$banana

# BWM sorted lexicographically:
$banana
a$banan
ana$ban
anana$b
banana$
na$bana
nana$ba

# BWT (last coloumn of BWM):
annb$aa
Examples
bw_transform("banana$") ➞ "annb$aa"

bw_transform("mississippi$") ➞ "ipssm$pissii"

bw_transform("acccgtttgtttcaatagatccatcaa$") ➞ "aacc$tacgttctaccatcaatatttgg"
Notes
Consider "$" as the terminator character at the end of every input text.

"""


def left_shift(text, n):
    return text[n:] + text[:n]


def bw_transform(string):
    bwm = sorted([left_shift(string, i) for i in range(0, len(string))])
    return ''.join([element[-1] for element in bwm])


assert bw_transform("banana$") == 'annb$aa'
assert bw_transform("mississippi$") == "ipssm$pissii"
assert bw_transform("acccgtttgtttcaatagatccatcaa$") == "aacc$tacgttctaccatcaatatttgg"
