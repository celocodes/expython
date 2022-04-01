from datetime import date
pessoa = dict()
pessoa['Nome'] = str(input('\nDigite o nome: '))
nasc = int(input('Digite o ano de nascimento: '))
pessoa['Idade'] = date.today().year - nasc
pessoa['CTPS'] = int(input('Digite o número da sua CTPS [0 se não tem]: '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o salário: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - date.today().year)
print()
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
