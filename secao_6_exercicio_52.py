"""
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas
notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas
notas de 100,50,20,10,5,2 e 1 real
"""

def sacar_nota(saque, nota):
    """
    Função recebe o valor do saque e o valor da nota. Devolve quantas notas devem ser dadas e quanto ainda falta
    para completar o valor
    """
    return int(saque / nota), saque % nota

saque = int(input("Valor a sacar:"))

notas = {}
if saque > 100:
    notas[100], saque = sacar_nota(saque, 100)
if saque > 50:
    notas[50], saque = sacar_nota(saque, 50)
if saque > 20:
    notas[20], saque = sacar_nota(saque, 20)
if saque > 10:
    notas[10], saque = sacar_nota(saque, 10)
if saque > 5:
    notas[5], saque = sacar_nota(saque, 5)
if saque > 2:
    notas[2], saque = sacar_nota(saque, 2)
if saque > 1:
    notas[1], saque = sacar_nota(saque, 1)

print(notas)
