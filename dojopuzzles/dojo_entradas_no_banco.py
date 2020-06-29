"""
http://dojopuzzles.com/problemas/exibe/entradas-no-banco/#
Todas as vezes que alguém passa na porta do maior banco da cidade de Pirenópolis, é gravado em um arquivo de log a data
e a hora da abertura da porta.
Cada registro no arquivo de log possui o seguinte formato:
[YYYY-mm-dd H:i:s] - Abertura da Porta OK

O gerente do banco precisa saber quantas pessoas entraram no banco no horário de expediente, para isso ele solicitou
que você faça um programa que verifique se o registro de entrada é válido e se a hora se encontra dentro do intervalo
de funcionamento do banco, das 10:00:00 até as 16:00:00.
"""

from random import randint


# Cria o evento de entrada para armazenar no log com dados randomicos
def evento_log(porta):
    return "[2020-05-27 " + str(randint(7, 18)) + ":" + str(randint(0, 59)) + ":00] - Abertura da Porta " + porta


# Criando log
log = [evento_log('NOK') if numero % randint(2, 5) == 0 else evento_log('OK') for numero in range(1, 20)]

# Imprimindo log para verificação
for i in range(len(log)):
    print(log[i])

pessoas = 0
# Implementação da contagem de pessoas que entraram no banco
for registro in log:
    abertura = registro.split('-')[3].split('Abertura da Porta ')[1]
    if abertura == 'OK':
        hora = int(registro.split('-')[2].split()[1].split(':')[0])
        if 10 <= hora < 16:
            pessoas += 1

print(f'Durante o horário de funcionamento, passaram {pessoas} pessoas pela porta')
