ter = int(input('\nDigite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
con = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while con <= total:
        if con == 1:
            print('\nOs 10 primeiros termos dessa progressão são: \n({}, '.format(ter), end='')
        elif con < total:
            print('{}, '.format(ter), end='')
        else:
            print('{}).'.format(ter))
        ter += raz
        con += 1
    mais = int(input('\nQuer ver mais termos? Digite quantos(0 para parar): '))
    print('...' if mais > 0 else '', end='')
print('\nParei! {} termos da PA foram mostrados.'.format(total))
