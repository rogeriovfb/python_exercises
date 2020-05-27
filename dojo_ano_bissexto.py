"""
http://dojopuzzles.com/problemas/exibe/ano-bissexto/
A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas
(mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo).
Para compensar essa diferença e evitar um descompasso em relação às estações do ano, insere-se um dia extra no
calendário e o mês de fevereiro fica com 29 dias. Essa correção é especialmente importante para atividades atreladas
às estações, como a agricultura e até mesmo as festas religiosas.

Um determinado ano é bissexto se:

O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.

São bissextos por exemplo:
1600, 1732, 1888, 1944, 2008
Não são bissextos por exemplo:
1742, 1889, 1951, 2011
Escreva uma função que determina se um determinado ano informado é bissexto ou não.
"""


def eh_bissexto(ano):
    if (not ano % 4 and ano % 100) or not ano % 400:
        return True
    else:
        return False


lista_anos = [1600, 1732, 1888, 1944, 2008, 1742, 1889, 1951, 2011]
print(list(map(eh_bissexto, lista_anos)))
