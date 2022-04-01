from datetime import date
totmen = 0
totmai = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if (date.today().year - nasc) < 21:
        totmen += 1
    elif (date.today().year - nasc) >= 21:
        totmai += 1
print('\nMenores de idade: {}'.format(totmen))
print('\nMaiores de idade: {}'.format(totmai))
