# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

dis = float(input('Digite a distância da viagem(em km): '))

# preço = dis * 0.50 if dis <=200 else dis * 0.45

if dis <= 200:
    print('O preço da passagem será: R${:.2f}'.format(0.50 * dis))
else:
    print('O preço da passagem será: R${:.2f}'.format(0.45 * dis))
