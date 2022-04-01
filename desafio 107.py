from módulos import moeda

p = float(input(f'\nDigite o preço: R$'))
print(f'\nA metade de {p} é {moeda.metade(p):.2f}')
print(f'O dobro de {p} é {moeda.dobro(p):.2f}')
print(f'O valor de {p}, com 10% de aumento, é {moeda.aumentar(p, 10):.2f}')
