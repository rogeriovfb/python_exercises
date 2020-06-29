"""
Faça uma função que receba um vetor de reais e retorne a média dele
"""

from statistics import mean


def media(*args):
    return mean(args)


dados = [0, 10, 20, 30, 40, 50]
print(media(*dados))
