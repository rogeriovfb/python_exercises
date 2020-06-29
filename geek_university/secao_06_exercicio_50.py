"""
Chico tem 1.50 metro e cresce 2 centimetros por ano. Zé tem 1.10 metro e cresce 3 centimetros por ano. Quantos
anos serão necessários para que zé seja maior que chico?
"""

altura_chico = 1.50
altura_ze = 1.10
anos = 0

while altura_ze <= altura_chico:
    anos +=1
    altura_ze += 0.03
    altura_chico += 0.02

print(f'Serão necessários {anos} anos para que Zé seja maior que Chico')
