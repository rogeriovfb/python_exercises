"""
Faça um programa que calcule a soma de todos numeros primos abaixo de dois milhões
"""

maximo = 20000
primos = [2]

for num in range(3, maximo+1):
    for i in range(2, num):
        if num % i == 0:
            break
        elif i > num/2:
            primos.append(num)
            break

# print(primos)
print(f'O somátorio de todos numeros primos abaixo de {maximo} é {sum(primos)}.')
