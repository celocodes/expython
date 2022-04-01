mai18 = hom = mulmen20 = 0
while True:
    idade = int(input('\nDigite a idade: '))
    sexo = opr = ' '
    while sexo not in 'MF':  # MUHFUCKA
        sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]
    if idade > 18:
        mai18 += 1
    if sexo == 'M':
        hom += 1
    if idade < 20 and sexo == 'F':
        mulmen20 += 1
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
print(f'\nPessoas com mais de 18 anos: {mai18}\nHomens cadastrados: {hom}\nMulheres com menos de 20 anos: {mulmen20}')
