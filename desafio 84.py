pessoas = []
dados = []
menor = maior = 0
while True:
    dados.append(str(input('\nDigite o nome: ')).strip())
    dados.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
print(f'\nNúmero de pessoas cadastradas: {len(pessoas)}')
print(f'\nO maior peso foi {maior}kg, de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menor}kg, de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
