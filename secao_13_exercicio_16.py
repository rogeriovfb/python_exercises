"""
Faça um programa que recebe um vetor de 10 numeros, converta cada um desses numeros para binario e grave a sequencia
de 0s e 1s em um arquivo txt. Cada numero deve ser gravado em uma linha.
"""

from random import randint

entrada = [randint(0, 255) for i in range(1, 11)]

print(entrada)

with open('secao_13_exercicio_16.txt', 'w') as arquivo:
    for num in entrada:
        arquivo.write("{0:08b}".format(num) + '\n')
