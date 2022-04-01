from time import sleep


def maior(*num):
    if len(num) > 0:
        print('\nNúmeros inseridos: ', end='')
        for n in num:
            print(f'{n} ', end='')
            sleep(0.25)
        num = sorted(num)
        print(f'\nTotal de valores: {len(num)}\nMaior valor: {num[-1]}')
    else:
        print('\nNenhum número foi inserido.\nMaior valor: 0')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
