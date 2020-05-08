"""
Faça uma função não-recursiva que receba um numero inteiro positivo N e retorne o superfatorial desse numero.
O superfatorual de N é o produto dos N primeiros fatoriais de N
"""


def fatorial(numero):
    """Retorna o fatorial do número passado como parâmetro"""
    resultado = 1
    for i in range(1, numero+1):
        resultado = resultado * i
    return resultado


def super_fatorial (numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado = resultado * fatorial(i)
    return resultado


print(super_fatorial(4))
print(super_fatorial(5))
print(super_fatorial(10))
