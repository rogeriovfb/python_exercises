"""Faça um programa que leia um numero inteiro N e depois imprima os N primeiros naturais impares"""

n = int(input('Insira N:'))

for i in range(1, n+1):
    print(2*i-1)
