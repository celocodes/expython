# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

n = str(input('Digite um nome inteiro: ')).strip

nome = n.split()

print('Nome digitado: {}'.format(n))
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))  # mostra o último nome da lista
