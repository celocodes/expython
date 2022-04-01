# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cid = str(input('Digite o nome de uma cidade brasileira: ')).strip().split()

pnome = cid[0]
tes = 'SANTO' in pnome.upper()

print('A cidade começa com o nome "SANTO"?', tes)

# RESOLUÇÃO DO PROF
# cid = str(input('Em que cidade você nasceu? ')).strip()
# print(cid[:5].upper() == 'SANTO')