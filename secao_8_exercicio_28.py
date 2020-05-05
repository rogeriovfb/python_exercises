"""
Faça uma função que receba como parametro o valor de um angulo em graus e calcule o valor do cosseno desse angulo
usando a série de Taylos (truncar em n=5). Use pi = 3.141593
"""

pi = 3.141593


def fatorial(numero):
    """Retorna o fatorial do número passado como parâmetro"""
    resultado = 1
    for i in range(1, numero+1):
        resultado = resultado * i
    return resultado


def elemento(x, n):
    """Calcula o enésimo elemento da série de Taylor para o cosseno de x (em radiano)"""
    return x**(2*n)*((-1)**n)/fatorial(2*n)


def degree_para_rad(deg):
    "Recebe um angulo em graus como parametro e retorna o valor em radianos"
    return deg*pi/180


def cosseno(degree):
    """Retorna o cosseno do angulo informado calculado pela série de taylor até n=5"""
    angulo_rad = degree_para_rad(degree)
    cos = 0
    for i in range(0, 6):
        cos = cos + elemento(angulo_rad, i)
    return cos


print(cosseno(0))
print(cosseno(45))
print(cosseno(60))
print(cosseno(90))
print(cosseno(180))
