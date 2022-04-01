numero = int(input('\nDigite um número inteiro: '))
escolha = int(input('Converter para binário(1), octal(2) ou hexadecimal(3)? Digite o número correspondente: '))
if escolha == 1:
    print('O número {} convertido para binário é igual a {}.'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} convertido para octal é igual a {}.'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número {} convertido para hexadecimal é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')
