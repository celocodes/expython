# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número inteiro de 0 a 9999: '))

print('\nO número {} tem:'.format(n))

# Versão usando str
#n = str(input('Digite um número inteiro de 0 a 9999: '))
#uni = n[3:4]
#dez = n[2:3]
#cen = n[1:2]
#mil = n[0:1]

# Versão usando int
uni = n // 1    % 10
dez = n // 10   % 10
cen = n // 100  % 10
mil = n // 1000 % 10

print('\nUnidade: {}'.format(uni))
print('Dezena: {:>2}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {:>2}'.format(mil))
