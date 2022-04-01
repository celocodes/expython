numeros = []
impar = []
par = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)
    opr = ' '
    while opr not in 'SN':
        opr = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if opr == 'N':
        break
print(f'\nNúmeros pares digitados: {par}\nNúmeros ímpares digitados: {impar}\nNúmeros digitados: {numeros}')
