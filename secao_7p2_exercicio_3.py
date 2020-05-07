"""
Faça um programa que preencha uma matriz 4x4 com o produto do valor da linha e da coluna de cada elemento
Em seguida, imprima a matriz na tela
"""


def imprime_matriz(listas):
    for lista in listas:
        print(lista)


matriz = []

for linha in range(1,5):
    lin = []
    for coluna in range(1,5):
        lin.append(linha*coluna)
    matriz.append(lin)

imprime_matriz(matriz)
