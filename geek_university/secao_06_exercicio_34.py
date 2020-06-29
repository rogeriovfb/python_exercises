"""
Faça um programa que calcule o menor numero divisível por cada um dos numero de 1 a 20 sem sobrar resto

"""

maximo_divisor = 20
numero = maximo_divisor
encontrado = False

while not encontrado:
    numero += maximo_divisor
    for i in range(2, maximo_divisor+1):
        if numero % i > 0:
            break
        elif i == maximo_divisor:
            encontrado = True;
print(numero)