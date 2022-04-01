numeros = [[], []]
for c in range(0, 7):
    num = int(input(f'\nDigite o {c+1}° valor: ' if c == 0 else f'Digite o {c+1}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)
print(f'\nValores pares: {sorted(numeros[0])}\nValores ímpares: {sorted(numeros[1])}')
