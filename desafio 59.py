from time import sleep
num1 = int(input('\nDigite um valor: '))
maior = num1
num2 = int(input('Digite mais um valor: '))
oper = 0
while oper != 5:
    oper = int(input('\nO que você quer fazer com esses dois valores?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos'
                     ' números\n[5] Sair\nDigite aqui: '))
    if oper == 1:
        print('\nA soma de {} e {} é igual a {}'.format(num1, num2, num1 + num2))
    elif oper == 2:
        print('\nO produto de {} e {} é igual a {}'.format(num1, num2, num1 * num2))
    elif oper == 3:
        if num2 > num1:
            maior = num2
        print('\nO maior valor entre {} e {} é {}'.format(num1, num2, maior))
    elif oper == 4:
        num1 = int(input('\nDigite um valor: '))
        num2 = int(input('Digite mais um valor: '))
    elif oper == 5:
        print('\nOk, finalizando!')
    else:
        print('\nDigite uma opção válida.')
    sleep(2)
