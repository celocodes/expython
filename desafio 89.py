boletim = []
while True:
    nome = str(input('\nDigite o nome: ')).strip().title()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    boletim.append([nome, [nota1, nota2], (nota1+nota2)/2])
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
print(f'\n{"BOLETIM GERAL":-^30}\n{"No.":<4}{"Nome":<20}{"Média":>6}\n{"-"*30}')
for al in boletim:
    print(f'{boletim.index(al):<4}{al[0]:<20}{al[2]:>6}')
print('-'*30)
while True:
    opr = int(input('\nMostrar nota de aluno específico(999 para parar): '))
    if opr == 999:
        print('Flw aí!!!')
        break
    if opr <= len(boletim) - 1:
        print(f'As notas de {boletim[opr][0]} são {boletim[opr][1]}')
