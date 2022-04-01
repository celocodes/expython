# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27

print('\nQuantos dólares você pode comprar? Descubra!\n')

d = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Você pode comprar um total de {:.2f} dólares.'.format(d/3.27))
