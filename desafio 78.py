numeros = []
for con in range(0, 5):
    num = int(input(f'Digite o número da posição {con}: '))
    numeros.append(num)
print(f'\nOs números que você digitou são {numeros}')
ord = sorted(numeros)
print(f'O menor número é {ord[0]} e aparece nas posições', end=' ')
for cont, num in enumerate(numeros):
    if num == ord[0]:
        print(f'{cont}', end=' ')
print(f'\nO maior número é {ord[-1]} e aparece nas posições', end=' ')
for cont, num in enumerate(numeros):
    if num == ord[-1]:
        print(f'{cont}', end=' ')
print()
