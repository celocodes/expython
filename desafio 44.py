precoprod = float(input('\n\033[1;36mDigite o preço do produto: '))
print('\n\033[1;34mMétodo de pagamento:\033[m \n\n\033[1;33mÀ vista com dinheiro(1) \nÀ vista no cartão(2) \n2x no '
      'cartão(3) \n3x ou mais no cartão(4)\n\033[m')
condpag = int(input('\033[1;36mDigite o número correspondente à sua escolha: \033[1;32m'))
if condpag == 1:
    print('\nO produto à vista, com 10% de desconto, custará R${:.2f}'.format(precoprod * 0.90))
elif condpag == 2:
    print('\nO produto à vista no cartão, com 5% de desconto, custará RS{:.2f}'.format(precoprod * 0.95))
elif condpag == 3:
    print('\nO produto em 2x no cartão, custará R${:.2f} com parcelas de R${:.2f} sem juros.'.format(precoprod, precoprod/2))
elif condpag == 4:
    numparc = int(input('\033[1;36mDigite o número de parcelas: \033[1;32m'))
    print('\nO produto em {}x no cartão, custará R${:.2f} com parcelas de R${:.2f}({}x) com juros.'
          .format(numparc, precoprod * 1.20, precoprod/numparc, numparc))
else:
    print('\n\033[1;31mOpção inválida.\033[m')
