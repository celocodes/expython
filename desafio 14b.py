#  Escreva um programa que converta uma temperatura digitada em graus Celsius e converta
#  para graus Fahrenheit.

print('\nConversor de Graus Fahrenheit para Graus Celsius\n')

f = float(input('Digite a temperatura em °F: '))
c = (f - 32) / 1.8

print('{}°F convertido para a escala Celsius é igual a {}°C.'.format(f, c))
