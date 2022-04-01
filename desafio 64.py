con = val = soma = 0
val = int(input('\nDigite um número inteiro(999 para parar): '))
while val != 999:
    con += 1
    soma += val
    val = int(input('Digite um número inteiro(999 para parar): '))
print('\nTotal de valores digitados: {}\nSoma dos valores: {}'.format(con, soma))
