"""
Four friends are playing a simple dice game (players are denoted p1, p2, p3 and p4).
In each round, all players roll a pair of six-sided dice. The player with the lowest total score is removed.
If the lowest score is shared by two or more players, the player in that group with the lowest score from their
first die is removed. If the lowest score is still shared (i.e. two or more players have the same rolls in the same
order), then all players roll again. This process continues until one player remains. Given a list of scores only
(given in player order for each round), return the winning player.

Example
dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]) ➞ "p1"

             p1      p2      p3      p4
Round 1 -> (6, 2), (4, 3), (3, 4), (5, 4)  Player 3 removed.
Round 2 -> (3, 5), (1, 5),         (4, 3)  Player 2 removed.
Round 3 -> (1, 5),                 (1, 5)  No lowest score, players roll again.
Round 4 -> (5, 6),                 (2, 2)  Player 1 wins!
Notes
"""


def dice_game(scores):
    players = {'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0}
    while len(players) > 1:
        minimum = {'p0': (7, 7)}
        for player in players:
            if sum(scores[0]) < sum(list(minimum.values())[0]):
                minimum = {player: scores[0]}
            elif sum(scores[0]) == sum(list(minimum.values())[0]):
                if scores[0][0] < list(minimum.values())[0][0]:
                    minimum = {player: scores[0]}
                elif scores[0][0] == list(minimum.values())[0][0]:
                    minimum = {'p0': scores[0]}
            scores.pop(0)
        players.pop(list(minimum.keys())[0], None)
    return list(players.keys())[0]


assert dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]) == "p1"
assert dice_game([(1, 3), (2, 6), (6, 3), (5, 6), (2, 2), (5, 6), (5, 4), (1, 3), (5, 6)]) == 'p4'
assert dice_game([(4, 4), (4, 3), (1, 1), (1, 1), (3, 1), (4, 5), (2, 6), (2, 3), (1, 5), (5, 3), (4, 5), (5, 2),
                  (2, 1)]) == 'p3'
assert dice_game([(6, 1), (4, 3), (2, 5), (1, 4), (6, 2), (2, 5), (1, 4), (6, 4), (4, 3)]) == 'p1'
assert dice_game([(1, 2), (2, 1), (4, 4), (1, 2), (1, 3), (1, 5), (2, 1), (4, 1), (5, 6), (5, 1), (4, 2), (5, 2),
                  (5, 1)]) == 'p1'
assert dice_game([(1, 2), (5, 6), (1, 3), (6, 5), (4, 6), (1, 3), (1, 3), (5, 3), (4, 1), (1, 1), (3, 3),
                  (4, 1)]) == 'p2'
assert dice_game([(1, 2), (2, 3), (5, 4), (4, 4), (5, 2), (1, 1), (3, 6), (4, 4), (2, 2)]) == 'p2'
assert dice_game([(1, 4), (4, 2), (3, 5), (4, 2), (1, 2), (1, 2), (2, 4), (3, 5), (4, 1), (2, 2), (1, 1), (1, 1),
                  (4, 3), (1, 1)]) == 'p2'
assert dice_game([(2, 6), (3, 6), (6, 3), (6, 5), (4, 5), (5, 3), (5, 6), (2, 6), (6, 5)]) == 'p4'
assert dice_game([(1, 1), (4, 3), (2, 1), (6, 2), (3, 2), (3, 2), (4, 2), (2, 1), (6, 5), (6, 2), (4, 5), (4, 5),
                  (5, 3), (3, 3)]) == 'p3'
assert dice_game([(5, 1), (2, 6), (1, 6), (6, 4), (3, 4), (2, 5), (6, 1), (3, 2), (4, 1)]) == 'p4'
assert dice_game([(1, 4), (3, 6), (1, 6), (6, 1), (4, 1), (4, 3), (6, 5), (5, 6), (5, 6), (2, 1), (2, 4)]) == 'p4'
assert dice_game([(1, 3), (6, 5), (5, 4), (5, 4), (2, 2), (4, 6), (4, 1), (5, 5), (4, 5)]) == 'p3'
assert dice_game([(2, 3), (3, 6), (5, 4), (3, 1), (2, 5), (1, 5), (5, 3), (4, 3), (2, 1)]) == 'p1'
assert dice_game([(4, 2), (4, 4), (1, 4), (1, 4), (1, 3), (3, 5), (6, 5), (1, 2), (5, 1), (6, 1), (2, 4), (2, 4),
                  (5, 4)]) == 'p2'
assert dice_game([(2, 5), (4, 1), (2, 1), (4, 4), (6, 5), (4, 4), (1, 4), (3, 1), (1, 5)]) == 'p2'
assert dice_game([(6, 3), (5, 5), (2, 3), (6, 6), (2, 5), (5, 1), (4, 4), (2, 2), (1, 3)]) == 'p1'
assert dice_game([(6, 2), (6, 1), (6, 1), (2, 2), (1, 1), (4, 3), (2, 6), (4, 6), (4, 6), (3, 4), (3, 5)]) == 'p3'
assert dice_game([(1, 6), (3, 2), (3, 4), (1, 2), (4, 1), (4, 2), (2, 5), (4, 1), (5, 1)]) == 'p3'
assert dice_game([(3, 4), (2, 5), (5, 5), (2, 5), (6, 4), (6, 5), (6, 2), (6, 2), (3, 5), (6, 4), (4, 2), (5, 2),
                  (3, 2), (6, 4), (1, 2), (5, 4), (5, 5)]) == 'p2'
assert dice_game([(1, 5), (3, 1), (2, 3), (5, 3), (1, 2), (1, 2), (6, 3), (2, 2), (6, 3), (2, 2), (5, 5), (3, 1),
                  (3, 1), (6, 6), (6, 4), (5, 3), (3, 4), (6, 4)]) == 'p3'