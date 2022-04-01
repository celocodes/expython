soma = maisde1000 = con = 0
print('\nLOJÃO DO CELÃO, SEM PRESSÃO')
while True:
    nome = str(input('\nDigite o nome do produto: ')).strip().title()
    preco = float(input('Digite o preço do produto: R$'))
    soma += preco
    if con == 0 or preco < menor:
        nomemenor = nome
        menor = preco
    if preco > 1000:
        maisde1000 += 1
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
    con += 1
print(f'\nTotal gasto: R${soma:.2f}\nNúmero de produtos que custam mais de R$1000.00: {maisde1000}')
print(f'O produto mais barato é {nomemenor}, que custa R${menor:.2f}')
