"""
Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui
"""

def quantos_pares(*args):
    pares = 0
    for numero in args:
        if numero % 2 == 0:
            pares += 1
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
print(quantos_pares(*numeros))

numeros2 = [2, 4, 6, 8, 10, 12, 14]
print(quantos_pares(*numeros2))
