def area(h, c):
    are = h * c
    print(f'\nA área de {h}x{c} é igual a {are:.2f}m².')


al = float(input('\nDigite o valor da altura: '))
co = float(input('Digite o valor do comprimento: '))
area(al, co)
