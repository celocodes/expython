while True:
    num = int(input('\nDigite um número para ver sua tabuada(Negativo para parar): '))
    if num < 0:
        break
    for con in range(1, 11):  # laço for economiza linhas
        print(f'\n{num} x {con:2} = {num*con}' if con == 1 else f'{num} x {con:2} = {num*con}')
print('\nTabuada finalizada!')
