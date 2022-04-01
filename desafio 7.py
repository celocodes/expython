# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))

m = (n1 + n2) / 2

print('A média entre {:.2f} e {:.2f} é igual a {:.2f}'.format(n1, n2, m))
