"""
Leia uma matriz 5x10 que se refere a respostas de 10 questoes de multipla escolha, referentes a 5 alunos. Leia tambem
um vetor de 10 posições contendo o gabarito de respostas, que podem ser a, b, c ou d. Emitir a nota correspondente
de cada aluno
"""

gabarito = ('a', 'b', 'c', 'd', 'c', 'a', 'b', 'c', 'd', 'c')

respostas = [['a', 'b', 'a', 'd', 'c', 'a', 'b', 'c', 'd', 'a'],
             ['b', 'b', 'b', 'd', 'c', 'a', 'b', 'c', 'd', 'b'],
             ['a', 'b', 'c', 'd', 'c', 'a', 'b', 'c', 'd', 'c'],
             ['b', 'b', 'd', 'd', 'c', 'c', 'b', 'c', 'd', 'd'],
             ['b', 'b', 'e', 'd', 'c', 'a', 'b', 'c', 'd', 'e']]

notas = []

for aluno in respostas:
    nota = 0
    for questao in range(0,10):
        if aluno[questao] == gabarito[questao]:
            nota += 1
    notas.append(nota)

print(notas)
