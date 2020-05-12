"""
Leia uma matriz 5x5. Leia um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final, escrever
a localização (linha e coluna) ou uma mensagem de "Não encontrado".
"""

from random import randint


def imprime_matriz(listas):
    for lista in listas:
        print(lista)


# Gerando a matriz 5x5
matriz = []
for i in range(1, 25, 5):
    numeros = []
    for k in range(0, 5):
        numeros.append(randint(0, 50))
    matriz.append(numeros)

imprime_matriz(matriz)

x = int(input('Insira o valor X a ser procurado na matriz acima: '))

encontrado = False
for linha in matriz:
    if x in linha:
        encontrado = True
        print(f'O valor está na linha {matriz.index(linha)}, coluna {linha.index(x)}')
        break

if encontrado is False:
    print('Valor não encontrado')
