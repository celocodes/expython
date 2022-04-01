saque = int(input('\nDigite o valor que deseja sacar: '))
sobra = saque
if saque >= 50:
    ced50 = int(saque/50)
    sobra = saque % 50
    print(f'\nCédulas de R$50: {ced50}')
if sobra >= 20:
    ced20 = int(sobra/20)
    sobra %= 20
    print(f'\nCédulas de R$20: {ced20}')
if sobra >= 10:
    ced10 = int(sobra/10)
    sobra %= 10
    print(f'\nCédulas de R$10: {ced10}')
if sobra >= 1:
    ced1 = int(sobra/1)
    print(f'\nCédulas de R$1: {ced1}')
