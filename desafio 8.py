# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

m = float(input('Digite um valor em metros: '))

print('O valor de {} em centimetros é igual a {:.0f}cm e em milimetros é igual a {:.0f}mm.'.format(m, m*100, m*1000))
