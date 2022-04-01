numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
numeros.sort(reverse=True)
print(f'\nTotal de valores digitados: {len(numeros)}\nLista de valores, em ordem decrescente: {numeros}')
print(f'O número 5 aparece {numeros.count(5)} vezes.' if 5 in numeros else f'O número 5 não aparece.')
