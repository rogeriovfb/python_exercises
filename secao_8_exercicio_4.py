"""
Faça uma função pra verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro, não
negativo que pode ser expresso como o quadrado de outro numero inteiro
"""

def quadrado_perfeito(num):
    if isinstance(num, float):
        return False
    for i in range(1, num):
        if i*i == num:
            return True
    return False


print(quadrado_perfeito(25.1))
print(quadrado_perfeito(25))
print(quadrado_perfeito(-25))
