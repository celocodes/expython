def ficha(nome, gols):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(gols) == 0 or gols.isnumeric() == False:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nom = str(input('Nome do jogador: ')).strip()
gol = str(input('Gols marcados: '))
ficha(nom, gol)
