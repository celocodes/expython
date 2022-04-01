lista = (int(input('Digite um número: ')), int(input('Digite mais um: ')), int(input('Digite outro: ')),
         int(input('Digite mais outro: ')))
print(f'Você digitou os valores {lista}')
print(f'Total de aparições do 9: {lista.count(9)}')
if 3 in lista:
    print(f'O primeiro 3 aparece na {lista.index(3) + 1}ª posição.')
else:
    print(f'O número 3 não apareceu :(')
print(f'Números pares: ', end='')
for num in lista:
    if num % 2 == 0:
        print(num, end=' ')
