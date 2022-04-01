nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print('O aluno foi \033[1;31mREPROVADO\033[m.')
elif 6.9 >= media > 5.0:
    print('O aluno está em \033[1;33mRECUPERAÇÃO\033[m.')
elif media >= 7.0:
    print('O aluno foi \033[1;32mAPROVADO\033[m!')
