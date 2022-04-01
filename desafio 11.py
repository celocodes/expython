# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

print('\nBora calcular a área da sua parede? Dá pra calcular o tanto de tinta que vai usar!\n')

la = float(input('Digite a largura da parede, em metros: '))
h = float(input('Digite a altura da parede, em metros: '))

a = la * h

print('A área da parede é igual a {:.2f}m² e a quantidade de tinta necessária é de {:.2f}L.'.format(a, a/2))
