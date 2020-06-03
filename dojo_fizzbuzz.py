"""
http://dojopuzzles.com/problemas/exibe/fizzbuzz/
Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""

lista = ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i
         for i in range(1, 101)]

for valor in lista:
    print(valor)
