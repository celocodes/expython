homidade = []
homnome = []
mulidademe20 = []
mulnome = []
idadetodos = []
for c in range(1, 5):
    nome = str(input('\nDigite o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa(M/F): '.format(c)))
    if sexo in 'Mm':
        homnome.append(nome)
        homidade.append(idade)
    elif sexo in 'Ff':
        mulnome.append(nome)
        if idade < 20:
            mulidademe20.append(idade)
    else:
        print('\nSexo inválido. Tente novamente.')
    idadetodos.append(idade)
med_ida = sum(idadetodos) / len(idadetodos)
maisvelho = sorted(homidade)
homidade2 = list(homidade)
nomemais = homidade2.index(maisvelho[-1])
print('\nA média de idade do grupo é igual a {} anos.'.format(med_ida))
print('\nO homem mais velho tem {1} anos e se chama {0}.'.format(homnome[nomemais], maisvelho[-1]))
print('\nNúmero de mulheres com menos de 20 anos: {}'.format(len(mulidademe20)))
