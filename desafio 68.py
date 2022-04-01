from random import randint
total = 0
while True:
    jognum = int(input('\nIMPOU PAR!\nDigite um número: '))
    com = randint(0, 10)
    jogiop = ' '
    while jogiop not in 'IP':
        jogiop = str(input('Ímpar ou Par? (I/P): ')).strip().upper()[0]
    num = jognum + com
    if (num % 2 == 0 and jogiop == 'P') or (num % 2 == 1 and jogiop == 'I'):
        print(f'\nO jogador venceu!\n\nEscolha do computador: {com}\nSua escolha: {jognum}\nSoma: {com + jognum}')
        total += 1
    elif (num % 2 == 1 and jogiop == 'P') or (num % 2 == 0 and jogiop == 'I'):
        print(f'\nO computador venceu!\n\nEscolha dele: {com}\nEscolha do Jogador: {jognum}\nSoma: {com + jognum}')
        break
print(f'\nGAME OVER! O jogador ganhou {total} vez!' if total == 1 else f'GAME OVER! O jogador ganhou {total} vezes!')
