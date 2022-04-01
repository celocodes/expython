ter = int(input('\nDigite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
con = 1
while con <= 10:
    if con == 1:
        print('\nOs 10 primeiros termos dessa progressão são: ({}, '.format(ter), end='')
    elif con < 10:
        print('{}, '.format(ter), end='')
    else:
        print('{}).'.format(ter))
    ter += raz
    con += 1
