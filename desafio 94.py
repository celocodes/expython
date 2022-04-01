grupo = []
pessoa = {}
soma = 0
while True:
    pessoa['nome'] = str(input('\nNome: ')).strip()
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo(M/F): ')).strip().upper()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
print(f'\n- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {soma/len(grupo)} anos.\n- As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print(f'\n- Lista de pessoas com idade acima da média: ')
for p in grupo:
    if p['idade'] > soma/len(grupo):
        print(f'\t', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
