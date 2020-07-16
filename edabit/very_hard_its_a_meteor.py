"""
In a video game, a meteor will fall toward the main character's home planet.
Given the meteor's trajectory as a string in the form y = mx + b and the character's position as a tuple of (x, y),
return True if the meteor will hit the character and False if it will not.

Examples
will_hit("y = 2x - 5", (0, 0)) ➞ False

will_hit("y = -4x + 6", (1, 2)) ➞ True

Notes
The b value will never be zero or blank.
The m value will always be an integer.
If the m value is 1, the "1" will be shown.
For example, "y = x + 5" will be shown as "y = 1x + 5".
If the m value is -1, the "-1" will be shown.
For example, "y = -x + 2" will be shown as "y = -1x + 2".
"""


def will_hit(equation, coord):
    m = int(equation.split(' ')[2].split('x')[0])
    b = int(equation.split(' ')[3] + equation.split(' ')[4])
    return coord[1] == m*coord[0] + b


assert will_hit("y = 2x - 5", (0, 0)) == False

assert will_hit("y = -4x + 6", (1, 2)) == True
