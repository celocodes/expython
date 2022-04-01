numeros = []
for con in range(0, 5):
    num = int(input('Digite um número: '))
    if con == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Número inserido no final da lista.')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Número inserido na posição {pos}.')
                break
            pos += 1
print(f'\nNúmeros inseridos, em ordem crescente: {numeros}')
