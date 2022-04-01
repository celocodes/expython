# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')

print('A classe de {} é'.format(a), type(a))

print('{} só tem espaços? '.format(a), a.isspace())
print('{} é um número? '.format(a), a.isnumeric())
print('{} é alfabético? '.format(a), a.isalpha())
print('{} é alfanumérico? '.format(a), a.isalnum())
print('{} só tem maiúsculas? '.format(a), a.isupper())
print('{} só tem minúsculas? '.format(a), a.islower())
print('{} está capitalizado? '.format(a), a.istitle())

# "a" é um objeto e tem características e realiza funcionalidades.
# Têm atributos e métodos. Por .is ter (), este é um método.
