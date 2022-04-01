con = soma = 0
while True:
    num = int(input('Digite um número(999 para parar): '))
    if num == 999:
        break
    con += 1
    soma += num
print(f'\nTotal de números digitados: {con}\nSoma dos valores: {soma}')
