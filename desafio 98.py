from time import sleep


def contador(inicio, fim, passo):
    passo = abs(passo)
    if passo == 0:
        passo = 1
    print(f'{"-"*30}\nContando de {inicio} a {fim} de {passo} em {passo}:')
    if inicio < fim:
        con = inicio
        while con <= fim:
            print(f'{con} ', end='')
            con += passo
            sleep(0.25)
    if inicio > fim:
        con = inicio
        while con >= fim:
            print(f'{con} ', end='')
            con -= passo
            sleep(0.25)
    print(f'\n{"-"*30}')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'\n{"-"*30}\nAgora é sua vez!')
ini = int(input('Início: '))
fin = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fin, pas)
