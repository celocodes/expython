    from random import randint
from time import sleep
print(f'\n{"="*45}\n{"BEGASEDA, HAHAI":^45}\n{"="*45}')
armaz = []
palpite = []
totpal = int(input('\nDigite quantos palpites devem ser gerados: '))
for ger in range(0, totpal):
    for jog in range(0, 6):
        num = randint(1, 60)
        for n in palpite:
            if num == n:
                num = randint(1, 60)
        palpite.append(num)
    armaz.append(sorted(palpite[:]))
    palpite.clear()
    print(f'Jogo {ger + 1}: {armaz[ger]}')
    sleep(1)
