"""
Faça uma função para calcular o número neperiano usando uma série.
A função deve ter como parametro o numero de termos que serão somados
"""


def fatorial(numero):
    """Retorna o fatorial do número passado como parâmetro"""
    resultado = 1
    for i in range(1, numero+1):
        resultado = resultado * i
    return resultado


def neperiano(n):
    """Retorna o número neperiano (e) calculado através de uma série com numero de termos informado como parametro"""
    resultado = 0
    for i in range(0,n+1):
        resultado = resultado + 1/(fatorial(i))
    return resultado


print(neperiano(0))
print(neperiano(3))
print(neperiano(5))
print(neperiano(10))
print(neperiano(20))
