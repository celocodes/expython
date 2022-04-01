from módulos import moeda

p = float(input(f'\nDigite o preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'O valor de {moeda.moeda(p)}, com 10% de aumento, é {moeda.aumentar(p, 10, True)}')
print(f'O valor de {moeda.moeda(p)}, com 13% de desconto, é {moeda.diminuir(p, 13, True)}')
