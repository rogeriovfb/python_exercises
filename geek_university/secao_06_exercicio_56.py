"""
Faça um programa que calcule a soma de todos numeros primos abaixo de dois milhões
"""

maximo = 2000000
soma = 0
for num in range(3, maximo+1, 2):
    for i in range(2, num):
        if num % i == 0:
            break
        elif i > num/2:
            soma += num
            break

print(f'O somátorio de todos numeros primos abaixo de {maximo} é {soma}.')
