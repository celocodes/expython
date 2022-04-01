from random import randint
ran = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'\nNúmeros gerados: {ran}')
print(f'Menor valor: {sorted(ran)[0]}\nMaior valor: {sorted(ran)[-1]}')
