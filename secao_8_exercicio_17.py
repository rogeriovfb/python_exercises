"""
Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos N números inteiros
existentes entre eles
"""


def soma_entre(a,b):
    if a < 0 or b < 0:
        return -1
    if not (isinstance(a, int) and isinstance(b, int)):
        return -1
    soma = 0
    for i in range(a+1, b):
        soma = soma + i
    return soma


print(soma_entre(-1,5))
print(soma_entre(1.5,5))
print(soma_entre(1,5))
