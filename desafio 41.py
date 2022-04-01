from datetime import date
anonasc = int(input('\nDigite o ano de nascimento do atleta: '))
idade = date.today().year - anonasc
if idade <= 9:
    print('Este atleta está na \033[1;30mcategoria\033[m \033[1;36mMIRIM\033[m.')
elif idade <= 14:
    print('Este atleta está na \033[1;30mcategoria\033[m \033[1;34mINFANTIL\033[m.')
elif idade <= 19:
    print('Este atleta está na \033[1;30mcategoria\033[m \033[1;33mJUNIOR\033[m.')
elif idade <= 25:
    print('Este atleta está na \033[1;30mcategoria\033[m \033[1;32mSÊNIOR\033[m.')
elif idade > 25:
    print('Este atleta está na \033[1;30mcategoria\033[m \033[1;31mMASTER\033[m.')
