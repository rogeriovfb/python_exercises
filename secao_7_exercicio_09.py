"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa
"""

lista = []

while len(lista) < 6:
    lista.insert(0, input(f'Número: '))

print(lista)
