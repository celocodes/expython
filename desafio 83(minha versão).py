exp = input('\nDigite uma expressão: ').strip()
if exp.count('(') == exp.count(')'):
    print('\nExpressão válida!')
else:
    print('\nExpressão inválida!')
