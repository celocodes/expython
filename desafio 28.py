# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o jogador venceu ou perdeu.

from random import randint

print('Tô pensando em um número entre 0 e 5...')

n = randint(0, 5)

ten = int(input('Tenta adivinhar: '))

if ten == n:
    print('Que legal, você acertou!')
else:
    print('Você errou. (voz do Silvio Santos)')

print('Eu pensei no número {}.'.format(n))
