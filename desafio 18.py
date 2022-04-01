# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.

import math

a = float(input('Digite um ângulo qualquer: '))

# Às vezes, pode ser que seja necessário ler o manual. O valor teria que ser convertido para radianos.

r = math.radians(a)

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O ângulo {}° ({:.3f} radianos) tem: '.format(a, r))
print('Um seno igual a {:.3f}'.format(s))
print('Um cosseno igual a {:.3f} \nE uma tangente igual a {:.3f}'.format(c, t))
