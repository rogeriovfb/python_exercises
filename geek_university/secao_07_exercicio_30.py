"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2 vetores
anterior sem números repetidos
"""

conj1 = set()
conj2 = set()

for i in range(1,11):
    conj1.add(int(input(f'Digite o {i}º número do primeiro vetor: ')))
    conj2.add(int(input(f'Digite o {i}º número do segundo vetor: ')))

resultado = conj1.intersection(conj2)

print(resultado)
