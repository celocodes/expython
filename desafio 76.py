lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Mochila', 120.32)
print(f'{"="*41}\n{"LISTA DE PREÇOS - LOJINHO DO CELINHO":^41}\n{"="*41}')
for con in range(0, len(lista), 2):
    print(f'|{lista[con]:.<30}', end='')
    print(f'R${lista[con+1] :>7.2f}|')
print(f'{"="*41}')
