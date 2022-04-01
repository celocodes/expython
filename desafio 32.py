# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Digite um ano qualquer(0 para ano atual): '))
if ano == 0:  # Condição SIMPLES
    ano = date.today().year
# if ano // 4 - int(ano // 4) == 0:  # EROUUUUUUUUUUUUU
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # - faltou lembrar do RESTO DA DIVISÃO (%)
    print('Esse ano({}) é bissexto.'.format(ano))
else:
    print('Esse ano({}) não é bissexto.'.format(ano))
