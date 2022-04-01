from time import sleep
from random import randint


def sorteia(lista):
    print(f'\nSorteando 5 valores: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)


def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'\nO resultado da soma dos valores pares de {lista} é {soma}.')


numeros = []
sorteia(numeros)
somapar(numeros)
