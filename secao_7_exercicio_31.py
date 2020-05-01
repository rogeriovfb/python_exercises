"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a uniao entre os 2 vetores anteriores,
ou seja, que contém os numeros dos dois vetores. Não deve conter numeros repetidos.

"""

conj1 = set()
conj2 = set()

for i in range(1,11):
    numero = int(input(f'Digite o {i}º número do primeiro vetor: '))
    if numero in conj1:
        print('Numero repetido, tente novamente')
    else:
        conj1.add(numero)
    numero = int(input(f'Digite o {i}º número do segundo vetor: '))
    if numero in conj2:
        print('Numero repetido, tente novamente')
    else:
        conj1.add(numero)

resultado = conj1.union(conj2)
print(resultado)
