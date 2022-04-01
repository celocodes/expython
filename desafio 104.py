

def leiaInt(mensagem):
    while True:
        num = str(input(mensagem))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print(f'\033[7;31mDigite um número inteiro!!!\033[m')
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acaba de digitar o número {n}.')
