soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1  # CONTADOR
        soma += c  # ACUMULADOR
print('\nA soma dos {} números é igual a {}.'.format(cont, soma))
