jogadores = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('\nNome do Jogador: ')).strip().title()
    partidas = int(input(f'Digite quantas partidas {jogador["nome"]} jogou: '))
    total = 0
    for p in range(0, partidas):
        quant = int(input(f'Gols na partida {p+1}: '))
        gols.append(quant)
        total += quant
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
print(f'\n{"No.":<4}{"Nome":<15}{"Gols":<18}{"Total":>6}\n{"-"*43}')
for j in jogadores:
    print(f'{str(jogadores.index(j)):<4}{str(j["nome"]):<15}{str(j["gols"]):<18}{str(j["total"]):>6}')
print('-'*43)
while True:
    opr = int(input('\nMostrar dados de jogador específico(999 para parar): '))
    if opr == 999:
        print('\nVOLTE SEMPRE!!!')
        break
    if opr <= len(jogadores) - 1:
        for j in jogadores:
            if jogadores.index(j) == opr:
                print(f'\nLEVANTAMENTO DO JOGADOR - {j["nome"]}')
                for n, g in enumerate(j['gols']):
                    print(f'\tNa partida {n+1}, fez {g} gols.')
    else:
        print('\nOpção inválida!')
