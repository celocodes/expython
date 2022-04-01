# Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira.

from math import trunc

n = float(input('Digite um número real: '))

print('O número {} tem a parte inteira {}.'.format(n, trunc(n)))
