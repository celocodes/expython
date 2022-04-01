from random import randint
from time import sleep
print('\n\033[1;32mJokenpô contra a Máquina!\033[m\n')
jog = int(input('\033[1;35mEscolha entre pedra(0), papel(1) e tesoura(2): \033[m'))
esc = ('pedra', 'papel', 'tesoura')
com = randint(0, 2)
print('\n\033[1;36mJO', end=' ')
sleep(0.5)
print('KEN', end=' ')
sleep(0.5)
print('PO!\033[m\033[1;33m')
sleep(0.25)
if jog == com:
    print('\nEmpate! Ambos escolheram {}!'.format(esc[com]))
elif (jog == 0 and com == 2) or (jog == 1 and com == 0) or (jog == 2 and com == 1):
    print('\nO jogador escolheu {} e o computador {}. O jogador venceu!'.format(esc[jog], esc[com]))
elif (com == 0 and jog == 2) or (com == 1 and jog == 0) or (com == 2 and jog == 1):
    print('\nO jogador escolheu {} e o computador escolheu {}. O computador venceu!'.format(esc[jog], esc[com]))
else:
    print('\n\033[1;31mOpção inválida. Tente novamente.\033[m')
