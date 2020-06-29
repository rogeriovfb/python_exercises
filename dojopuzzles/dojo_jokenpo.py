"""
http://dojopuzzles.com/problemas/exibe/jokenpo/
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens:
Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:

Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra
"""

from random import choice
from time import sleep


def juiz_jokenpo(jog1, jog2):
    if jog1 == jog2:
        return 'Empatou'
    elif jog1 == 'pedra' and jog2 == 'tesoura':
        return 'Jogador 1 ganhou'
    elif jog1 == 'papel' and jog2 == 'pedra':
        return 'Jogador 1 ganhou'
    elif jog1 == 'tesoura' and jog2 == 'papel':
        return 'Jogador 1 ganhou'
    else:
        return 'Jogador 2 ganhou'


print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!")
sleep(0.5)

jogador1 = choice(('pedra', 'papel', 'tesoura'))
jogador2 = choice(('pedra', 'papel', 'tesoura'))

print(f'O Jogador 1 colocou {jogador1}')
print(f'O Jogador 2 colocou {jogador2} \n')

print(juiz_jokenpo(jogador1, jogador2))
