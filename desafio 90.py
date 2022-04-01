aluno = {'Nome': str(input('Digite o nome: '))}
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 7 > aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
