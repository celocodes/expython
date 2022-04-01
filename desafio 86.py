matriz = [[], [], []]
for sis in range(0, 3):
    for con in range(0, 3):
        matriz[sis].insert(con, int(input(f'Digite o valor de [{sis}, {con}]: ')))
for lin in matriz:
    print(f'\n{lin[0]:7}  {lin[1]:7}  {lin[2]:7}' if lin == matriz[0] else f'{lin[0]:7}  {lin[1]:7}  {lin[2]:7}')
