matriz = [[], [], []]
somapar = somater = maior = 0
for sis in range(0, 3):
    for con in range(0, 3):
        num = int(input(f'Digite o valor de [{sis}, {con}]: '))
        matriz[sis].append(num)
        if num % 2 == 0:
            somapar += num
        if con == 2:
            somater += num
        if sis == 1:
            if con == 0 or num > maior:
                maior = num
for lin in matriz:
    print(f'\n{lin[0]:7}  {lin[1]:7}  {lin[2]:7}' if lin == matriz[0] else f'{lin[0]:7}  {lin[1]:7}  {lin[2]:7}')
print(f'\nSoma dos valores pares: {somapar}\nSoma dos valores da terceira coluna: {somater}')
print(f'Maior valor da segunda linha: {maior}')
