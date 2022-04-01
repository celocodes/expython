# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite um salário: R$'))

if sal > 1250.00:
    print('O valor do salário, com aumento de 10%, é igual a R${:.2f}'.format(sal * 1.10))
else:
    print('O valor do salário, com aumento de 15%, é igual a R${:.2f}'.format(sal * 1.15))
