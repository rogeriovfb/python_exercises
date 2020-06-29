"""
Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva a matriz obtida

"""


def imprime_matriz(matriz, linhas):
    for i in range(linhas):
        print(matriz[i])


n = 5
m = 5
matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

imprime_matriz(matriz, n)
