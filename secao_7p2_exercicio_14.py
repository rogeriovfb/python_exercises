"""
Faça um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de bingo.
A cartela possui 5 linhas e 5 colunas. Imprima a cartela gerada.
"""

from random import randint


def imprime_matriz(listas):
    for lista in listas:
        print(lista)


def lista_aleatoria(tamanho, menor_valor, maior_valor):
    resultado = []
    while len(resultado) < tamanho:
        elemento = randint(menor_valor, maior_valor)
        if elemento in resultado:
            continue
        else:
            resultado.append(elemento)
    return resultado


numeros = lista_aleatoria(25, 0, 99)
numeros.sort()
matriz = []

for i in range(0, len(numeros), 5):
    matriz.append(numeros[i:i + 5])

imprime_matriz(matriz)



