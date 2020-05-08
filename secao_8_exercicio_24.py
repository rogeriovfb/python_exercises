"""
Escreva uma função que gera um triangulo de altura e lados n e base 2*n-1
"""


def imprime_espaco(quantidade):
    """Função para imprimir espaços para centralizar os elementos do triangulo"""
    for num in range(quantidade):
        print(' ', end='')
    return


n = int(input('Digite o N do triangulo:'))

for i in range(1, n+1):
    imprime_espaco(n - i)  # A quantidade de espaços antes do elemento é metade da base menos a posicao da linha
    for k in range(1, 2 * i):
        print('*', end='')
    print()
