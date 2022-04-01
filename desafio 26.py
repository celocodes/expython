# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece pela primeira vez.
# Em que posição ela aparece pela última vez.

# LEMBRE-SE DE FAZER O PROGRAMA EM ETAPAS.

frase = str(input('Digite uma frase: ')).lower()  # - já irá armazenar como minúscula

print('\nNesta frase, a letra "a" aparece {} vezes.'.format(frase.count('a')))
print('Essa letra aparece primeiro na {}° posição.'.format(frase.find('a')+1))
print('Essa letra aparece por último na {}° posição.'.format(frase.rfind('a')+1))  # - acha da direita pra esquerda
