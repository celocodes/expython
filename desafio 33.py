# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro: '))
n3 = float(input('Digite mais um: '))

# Achando o menor número
menor = n1  # Para economizar uma linha e um teste
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Achando o maior número
maior = n1  # Para economizar uma linha e um teste
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {} e o maior é {}.'.format(menor, maior))
