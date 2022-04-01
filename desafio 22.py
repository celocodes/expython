# Crie um programa que leia o nome completo de uma pessoa e mostre:
# Nome em maiúsculo
# Nome em minúsculo
# Quantas letras no total(sem espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite um nome inteiro: ')).strip()

print('Nome somente com letras maiúsculas:', nome.upper())
print('Nome somente com letras minúsculas:', nome.lower())

pnome = nome.split()
# nome = nome.replace(' ', '')

print('Número de letras no nome:', len(nome) - nome.count(' ')) # largura do nome menos os espaços
print('Número de letras no primeiro nome:', len(pnome[0]))
