"""
Faça um programa para ler 10 números diferentes a serem armazenados em um vetor. Os dados deverão ser armazenados na
ordem que forem sendo lidos, sendo que caso o usuário digite um numero ja digitado, o programa deve pedir que digite
outro. Exibir na tela o vetor final que foi digitado.
"""

lista = []

while len(lista) < 10:
    numero = int(input(f'Digite o {len(lista)+1}º número: '))
    if numero in lista:
        print('Numero repetido, tente novamente')
    else:
        lista.append(numero)

print(lista)
