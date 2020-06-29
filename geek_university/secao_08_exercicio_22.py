"""
Crie uma função que receba como parametro um valor inteiro e gere como saída n linhas com pontos de exclamação.
"""


def exclamacao(n):
    for i in range(1, n+1):
        print('!'*i)


exclamacao(5)
