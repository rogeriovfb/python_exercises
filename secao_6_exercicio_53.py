"""
Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n linhas do triangulo de Floyd
"""

linhas = int(input('Insira o número de linhas do triângulo: '))
contador = 1

for k in range(1, linhas+1):
    print()
    for i in range(1, k+1):
        print(contador, end=' ')
        contador += 1
