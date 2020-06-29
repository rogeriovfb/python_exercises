"""
Faça uma função que receba duas strings e retorne a intercalação letra a letra da primeira com a segunda string
Retorne o resultado numa string

"""


def intercalacao(str1, str2):
    resultado = ''
    for tupla in list(zip(str1, str2)):
        for elemento in tupla:
            resultado = resultado + elemento
    return resultado


print(intercalacao('acegikmo', 'bdfhjlnp'))


