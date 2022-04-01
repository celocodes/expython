valorcasa = float(input('Digite o valor da casa que quer comprar: R$'))
salario = float(input('Digite seu salário: R$'))
anospag = int(input('Digite em quantos anos quer pagar a casa: '))
mensprest = valorcasa / (anospag * 12)
if mensprest > (salario * 0.3):
    print('Empréstimo negado. O valor da mensalidade excede 30% do seu salário.'.format(mensprest))
else:
    print('Empréstimo concedido! Você pagará R${:.2f} por mês durante {} anos.'.format(mensprest, anospag))
