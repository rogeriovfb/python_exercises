"""
Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado da seguinte serie:
S = 2/4 + 5/5 + 10/6 + ... + (N^2+1)/(N+3)
"""


def elemento(n):
    return (n**2 + 1)/(n+3)


N = int(input('Insira a quantidade de termos da série: '))
soma = 0

for i in range(1, N+1):
    soma = soma + elemento(i)

print(soma)
