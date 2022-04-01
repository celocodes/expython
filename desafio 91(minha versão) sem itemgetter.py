from random import randint
from time import sleep
jogadas = [{'Nome': 'Jogador 1', 'Jogada': randint(0, 6)}, {'Nome': 'Jogador 2', 'Jogada': randint(0, 6)},
           {'Nome': 'Jogador 3', 'Jogada': randint(0, 6)}, {'Nome': 'Jogador 4', 'Jogada': randint(0, 6)}]
ranking = []
con = 1
print('\nJogadas: ')
sleep(1)
for j in jogadas:
    print(f'O {j["Nome"]} tirou o número {j["Jogada"]}')
    sleep(1)
print('\nRanking: ')
sleep(1)
for j in jogadas:
    ranking.append(j['Jogada'])
    ranking.sort(reverse=True)
for n in ranking:
    if ranking.count(n) > 1:
        ranking.pop(ranking.index(n))
    for j in jogadas:
        if j['Jogada'] == n:
            print(f'{con}o lugar: {j["Nome"]} com {j["Jogada"]}.')
            con += 1
            sleep(1)