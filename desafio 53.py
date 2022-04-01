frase = str(input('\nDigite uma frase qualquer(sem acentos, por favor): ')).strip().upper()
frase = frase.replace(' ', '')
esarf = frase[::-1]
if frase == esarf:
    print('\nEsta frase é um palíndromo.')
else:
    print('\nEsta frase não é um palíndromo.')
