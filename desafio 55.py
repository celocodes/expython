pesos = []
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    pesos.append(peso)
pesos.sort()
print('O menor peso inserido foi {}kg e o maior foi {}kg'.format(pesos[0], pesos[-1]))
