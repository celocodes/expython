# Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.

n = int(input('Digite um número inteiro: '))

# MINHA VERSÃO
# if n/2 - int(n/2) == 0:
#    print('O número {} é par!'.format(n))
# else:
#    print('O número {} é ímpar!'.format(n))


# VERSÃO DO PROF
res = n % 2  # - resto da divisão por 2 será 0 para par e 1 para ímpar.
if res == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))
