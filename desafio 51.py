ter = int(input('\nDigite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
dec = ter + (10 - 1) * raz
for con in range(ter, dec + raz, raz):
    if con == ter:
        print('\nOs 10 primeiros termos dessa progressão são: \n({}, '.format(con), end='')
    elif con < dec:
        print('{}, '.format(con), end='')
    else:
        print('{}).'.format(con))
