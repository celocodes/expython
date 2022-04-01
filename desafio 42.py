print('\n\033[1;32mBora analisar uns triângulos?\033[m')
a = float(input('\n\033[1;35mDigite o comprimento do primeiro segmento:\033[m '))
b = float(input('\033[1;33mDigite o comprimento do segundo segmento:\033[m '))
c = float(input('\033[1;36mDigite o comprimento do terceiro segmento:\033[m '))
tes1 = abs(b - c) < a < (b + c)  # abs() seria o pipe na matemática que escrevemos, |b - c|
tes2 = abs(a - c) < b < (a + c)  # o professor usa um conceito matemático mais simplificado.
tes3 = abs(a - b) < c < (a + b)
triangulo = False
if tes1 and tes2 and tes3:
            print('\n\033[0;30mEstas retas podem formar um triângulo\033[m', end='')
            if a == b == c:
                print('\033[0;30m \033[0;35mequilátero\033[m.\033[m')
            if a == b != c or a == c != b or c == b != a:
                print('\033[0;30m \033[0;35misósceles\033[m.\033[m')
            if a != b != c != a:
                print('\033[0;30m \033[0;35mescaleno\033[m.\033[m')
else:
    print('\n\033[0;30mEstas retas \033[0;31mnão\033[m \033[0;30mpodem formar um triângulo.\033[m')
