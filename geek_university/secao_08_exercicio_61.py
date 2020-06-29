"""
Escreva uma função que compare e retorne verdadeiro, caso uma string seja anagrama de outra e falso, caso contrario
"""


def anagrama(str1, str2):
    lista1 = list(str1.lower())
    lista2 = list(str2.lower())
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    return False


print(anagrama('Conversationalists', 'Conservationalists'))
print(anagrama('The detectives', 'Detect thieves'))
print(anagrama('anagrama', 'batata'))
