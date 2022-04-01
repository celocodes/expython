# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('\nCalcule agora o quanto deve pagar de aluguel!\n')

km = float(input('Digite quantos km foram percorridos: '))
d = int(input('Digite por quantos dias o carro foi alugado: '))

p = (km * 0.15) + (d * 60)

print('\nValor total a pagar: R${:.2f}'.format(p))
