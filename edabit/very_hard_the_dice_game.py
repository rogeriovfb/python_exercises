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
    players = [(1, (0, 0)), (2, (0, 0)), (3, (0, 0)), (4, (0, 0))]
    while len(players) > 1:
        minimum = (0, (7, 7))
        for player in players:
            if sum(scores[0]) < sum(minimum[1]):
                minimum = (player[0], scores[0])
            elif sum(scores[0]) == sum(minimum[1]):
                if scores[0][0] < minimum[1][0]:
                    minimum = (player[0], scores[0])
                elif scores[0][0] == minimum[1][0]:
                    minimum = (0, scores[0])
            scores.pop(0)
        [players.remove(player) for player in players if player[0] == minimum[0]]
    return 'p' + str(players[0][0])


assert dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]) == "p1"
