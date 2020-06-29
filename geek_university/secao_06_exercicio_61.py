"""
Faça um programa que calcule o maior numero palindromo feito a partir do produto de dois numeros de 3 digitos.
"""

encontrado = False
valor1 = 999
valor2 = 999

while encontrado is False:
    resultado = str(valor1*valor2)
    inverso = resultado[::-1]
    if resultado == inverso:
        print(f'A multiplicação que resulta no maior palindromo é {valor1} * {valor2} = {resultado}')
        break
    elif valor1 == valor2:
        valor2 -= 1
    else:
        valor1 -=1
