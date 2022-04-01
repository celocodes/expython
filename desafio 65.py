num1 = int(input('\nDigite um número inteiro: '))
maior = menor = num1
con = 1
soma = 0
oper = str(input('Deseja continuar colocando números?(S/N): ')).strip().upper()
while oper == 'S':
    num2 = int(input('\nDigite um número inteiro: '))
    oper = str(input('Deseja continuar colocando números?(S/N): ')).strip().upper()
    if num2 > maior:
        maior = num2
    elif num2 < menor:
        menor = num2
    con += 1
    soma += num2
    num2 = num1
print('\nMédia de todos os {} valores: {}\nMaior inserido: {}\nMenor inserido: {}'.format(con, soma/con, maior, menor))
