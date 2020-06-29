"""
http://dojopuzzles.com/problemas/exibe/analisando-a-conjectura-de-collatz/

Para definir uma seqüência a partir de um número inteiro o positivo, temos as seguintes regras:

n → n/2 (n é par)

n → 3n + 1 (n é ímpar)

Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Podemos ver que esta seqüência (iniciando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha sido provado
(este problema é conhecido como Problema de Collatz), sabemos que com qualquer número que você começar,
a seqüência resultante chega no número 1 em algum momento.

Desenvolva um programa que descubra qual o número inicial entre 1 e 1 milhão que produz a maior seqüência.
"""


def elemento(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n / 2


def conta_termos_collatz(i):
    contador = 1
    while i != 1:
        i = elemento(i)
        contador += 1
    return contador


sequencia = {'inicial': 0, 'tamanho': 0}

for n in range(1, 1_000_001):
    tamanho = conta_termos_collatz(n)
    if tamanho > sequencia['tamanho']:
        sequencia = {'inicial': n, 'tamanho': tamanho}

print(sequencia)
