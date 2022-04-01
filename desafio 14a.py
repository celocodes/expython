#  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta
#  para graus Fahrenheit.

print('\nConversor de Graus Celsius para Graus Farenheit.\n')

c = float(input('Digite a temperatura em °C: '))

f = 1.8 * c + 32

print('{}°C convertido para a escala Farenheit é igual a {:.1f}°F.'.format(c, f))
