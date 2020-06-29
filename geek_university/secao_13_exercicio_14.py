"""
Dado um arquivo contendo um conjunto de nome e data de nascimento (DD MM AAAA), faça um programa que leia o nome do
arquivo e a data de hoje e construa outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo
"""

from io import StringIO
from datetime import datetime


def diferenca_anos(data):
    """
    :param data: Uma lista no formato [..., dd, mm, aaaa]
    :return: int do delta em anos entre o dia atual e a data recebida na função
    """
    return int((datetime.now() - datetime(year=int(data[-1]), month=int(data[-2]), day=int(data[-3]))).days/365.25)


# Arquivo de entrada simulado em memória
dados_entrada = 'João 01 05 2000\nMaria 04 06 2007\nJoão Pedro 25 12 1990\n'
entrada = StringIO(dados_entrada)

dados_saida = ''
for line in entrada:
    nome = line[:-12]
    idade = diferenca_anos(line.rstrip('\n').split(' '))
    dados_saida += nome + ' ' + str(idade) + ' anos\n'

# Arquivo de saída simulado em memória
saida = StringIO(dados_saida)

entrada.seek(0)
print(entrada.read())
print(saida.read())
