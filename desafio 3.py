# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o número que deseja somar ao primeiro: '))

# soma = n1 + n2

# print('A soma vale entre', n1, 'e', n2, 'vale', soma)

print('A soma entre {0} e {1} vale {2}'.format(n1, n2, n1+n2))

# Novamente, o .format() ajuda MUITO na formatação.
# Alinhamentos
#  {:20} - aparecer em 20 caracteres
# {:>20} ou {:<20} ou {:^20} - respectivamente, à direita ou à esquerda ou centralizado
# {:=^20} - centralizado com '=' nos lugares vazios

# int = inteiros
# float = flutuante/números reais
# bool = true e false, sem valor, fica como falso
# str = cadeia de caracteres

# no print (variavel.isalgumacoisa()) serve para testar coisas colocadas
# print(n.isalpha())  variável n é alfabética?
# se n for numérico, aparece True
