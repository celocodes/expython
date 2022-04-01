jogador = {'nome': str(input('\nNome do Jogador: ')).strip(), 'gols': list()}
partidas = int(input(f'Digite quantas partidas {jogador["nome"]} jogou: '))
for p in range(0, partidas):
    quant = int(input(f'\tGols na partida {p+1}: '))
    jogador['gols'].append(quant)
jogador['total'] = sum(jogador['gols'])
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'\nO jogador {jogador["nome"]} jogou {partidas} partidas.')
for n, g in enumerate(jogador['gols']):
    print(f'\tNa partida {n+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
