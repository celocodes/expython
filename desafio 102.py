from math import factorial


def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Diz se o processo da conta será ou não mostrado.
    :return: O valor do fatorial de n.
    """
    res = 1
    if show:
        print(f'\nO fatorial de {n} é:')
        while n >= 1:
            res *= n
            print(f'{n} x ', end='' if n != 1 else f'{n} = {res}\n')
            n -= 1
    else:
        print(f'\nO fatorial de {n} é: {factorial(n)}')


print()
help(fatorial)
fatorial(7, True)
fatorial(8)
