"""
Escreva um programa que:
a) Crie/abra um arquivo texto de nome arq.txt
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere 0
c) Feche o arquivo

Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados.
"""

with open('arq.txt', 'a') as arquivo:
    while True:
        entrada = input("Informe o dado a ser inserido no arquivo. '0' para sair:")
        if entrada != '0':
            arquivo.write(entrada + '\n')
        else:
            break

with open("arq.txt") as arquivo:
    for linha in arquivo:
        for caracter in linha:
            print(caracter, end='')
