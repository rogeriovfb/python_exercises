"""
Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos, e os converta
em segundos
"""


def minutos_para_segundos(minutos):
    return minutos*60


def hora_para_segundos(hora):
    return hora*60*60


def horario_para_segundos(hora, minutos, segundos):
    return segundos + minutos_para_segundos(minutos) + hora_para_segundos(hora)


# Teste da função
print(horario_para_segundos(1, 0, 0))
print(horario_para_segundos(1, 1, 0))
print(horario_para_segundos(1, 1, 1))
