# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot, sqrt

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = sqrt(pow(co, 2) + pow(ca, 2))
# hip = hypot(co, ca)

print('\nO comprimento da hipotenusa é igual a {:.3f}'.format(hip))
