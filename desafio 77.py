palavras = ('aprender', 'falar', 'andar', 'escrever', 'pular', 'cantar', 'dançar', 'sorrir', 'risada', 'brincar')
for p in palavras:
    print(f'\nA palavra {p.lower()} tem as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
