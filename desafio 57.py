sexo = str(input('\nDigite seu sexo(M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\nErro! Digite seu sexo novamente(M/F): ')).strip().upper()[0]
print('Sexo {} armazenado com sucesso.'.format(sexo))