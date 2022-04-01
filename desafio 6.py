# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número qualquer: '))

print('Dobro = {} \nTriplo = {} \nRaiz Quadrada = {:.2f}'.format(int(n*2), int(n*3), n**(1/2)))
