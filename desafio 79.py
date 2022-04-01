numeros = []
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso!')
    elif num in numeros:
        print('Duplicata! Este valor não será adicionado novamente.')
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
numeros.sort()
print(f'\nOs números digitados, em ordem crescente, são {numeros}.')
