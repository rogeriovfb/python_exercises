"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela
"""
conjunto = list()
repetidos = list()
for i in range(1,11):
    dado = int(input(f'Insira o {i}º valor:'))
    if dado in conjunto:
        repetidos.append(dado)
    else:
        conjunto.append(dado)

print(f'O conjunto de dados únicos é {conjunto} e foram repetidos os valores {repetidos}')
