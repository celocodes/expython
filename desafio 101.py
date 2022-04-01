def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    vot = 'VOTO OBRIGATÓRIO'
    if idade < 18:
        vot = 'NÃO VOTA'
    if idade > 65 or (18 > idade > 15):
        vot = 'VOTO OPCIONAL'
    print(f'Com {idade} anos: {vot}.')


nasc = int(input('\nDigite o ano em que você nasceu: '))
voto(nasc)
