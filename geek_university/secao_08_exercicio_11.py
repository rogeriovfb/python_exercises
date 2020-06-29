"""
Elabore uma função que receba três notas de um aluno como parâmetros e uma letra.
Se a letra for A, a função deverá calcular a média aritimética das notas; Se P, a média ponderada com pesos 5, 3 e 2.
"""
from statistics import mean


def media(*args, tipo='A'):
    """ Calcula a média dos valores. Se tipo = 'A' (default), retorna média aritimética. Se = 'P', média ponderada"""
    if tipo == 'A':
        return mean(args)
    elif tipo == 'P':
        peso = (0.5, 0.3, 0.2)
        return sum(peso[i] * args[i] for i in range(0, 3))


print(media(1, 2, 3))
print(media(1, 2, 3, tipo='P'))
