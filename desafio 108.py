from módulos import moeda

p = float(input(f'\nDigite o preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O valor de {moeda.moeda(p)}, com 10% de aumento, é {moeda.moeda(moeda.aumentar(p, 10))}')
