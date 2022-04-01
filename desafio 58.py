from random import randint
ten = 0
jog = -1
com = randint(0, 10)
while jog != com:
    jog = int(input('\nDigite um número entre 0 e 10: '))
    if jog != com:
        print('Erouuuuuuuu, tente novamente!')
    if jog > com:
        print('O número que pensei é menor!')
    elif jog < com:
        print('O número que pensei é maior!')
    ten += 1
print('Você acertou! O número era {} e você precisou de {} tentativas!'.format(com, ten))
