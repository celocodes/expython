# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro: '))

if vel <= 80.0:
    print('\nSem multa, campeão!')
else:
    print('\nVocê estava acima do limite de velocidade(80km/h) e terá que pagar R${:.2f}'.format((vel-80)*7))
