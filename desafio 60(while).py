from math import factorial
num = int(input('\nDigite um número para descobrir seu fatorial: '))
con = num
print('{}! = '.format(num), end='')
while con > 0:
    print(con, end='')
    print('x' if con > 1 else ' = ', end='')
    con -= 1
print('{}'.format(factorial(num)))
