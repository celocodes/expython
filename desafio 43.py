peso = float(input('\nDigite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('Seu IMC é de \033[1;35m{:.1f}\033[m'.format(imc), end=' ')
if imc < 18.5:
    print('e você está abaixo do peso ideal.')
if 25 > imc >= 18.5:
    print('e você está no peso ideal.')
if 25 >= imc > 30:
    print('e você tem um caso de sobrepeso.')
if 30 >= imc > 40:
    print('e você tem um caso de obesidade.')
if imc >= 40:
    print('e você está em obesidade mórbida.')
