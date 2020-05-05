"""
Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado da seguinte serie:
S = 2/4 + 5/5 + 10/6 + ... + (N^2+1)/(N+3)
"""


def elemento(k):
    return (k**2 + 1)/(k+3)


def somatorio_serie(n):
    soma = 0
    for i in range(1, n + 1):
        soma = soma + elemento(i)
    return soma


n = int(input('Insira a quantidade de termos da série: '))
print(somatorio_serie(n))
