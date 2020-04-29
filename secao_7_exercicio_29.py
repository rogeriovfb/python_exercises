"""
Seção 7 - Exercício 29

Faça um programa que receba 6 números inteiros e mostre:
    - Os números pares digitados;
    - A soma dos números pares digitados
    - Os números ímpares digitados
    - A quantidade de números ímpares digitados

"""

size = 0
par = []
impar = []

while size < 6:
    size += 1
    num = int(input(f'Digite o {size}º número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Os números pares são {par} e o somátorio é {sum(par)}')
print(f'Os números ímpares são {impar} e o somatório é {sum(impar)}')
