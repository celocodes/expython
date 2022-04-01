from datetime import date
anonasc = int(input('\nDigite o ano que você nasceu: '))
genero = int(input('Você é homem ou mulher? Digite 1 ou 2: '))
idade = date.today().year - anonasc
if genero == 2:
    print('\nVocê não precisa se alistar!')
elif idade < 18:
    print('\n{} aninhos! Você ainda vai se alistar, daqui a {} ano(s).'.format(idade, 18 - idade))
elif idade == 18:
    print('\nTá na hora de se alistar!')
elif idade > 18:
    print('\n{} aninhos! Você já passou do tempo do alistamento, faz {} ano(s).'.format(idade, idade - 18))

