times = ('Flamengo', 'Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense',
         'Athletico-PR', 'Bahia', 'Bragantino', 'Sport', 'Fortaleza', 'Corinthians', 'Ceará', 'Atlético-GO', 'Vasco',
         'Coritiba', 'Botafogo', 'Goiás')
print(f'Os primeiros 5 times do campeonato brasileiro são {times[:5]}')
print(f'Os últimos 4 colocados na tabela são {times[-4:]}')
print(f'Lista em ordem alfabética: {sorted(times)}')
print(f'O Palmeiras está na {times.index("Palmeiras") + 1}ª posição')
