num = int(input('Digite quantos elementos da Sequência de Fibonacci você quer ver: '))
con = 3
ter1 = 0
ter2 = 1
print('{}, {}, '.format(ter1, ter2), end='')
while con <= num:
    ter3 = ter1 + ter2
    if con < num:
        print('{}, '.format(ter3), end='')
    if con == num:
        print('{}...'.format(ter3), end='')
    ter1 = ter2
    ter2 = ter3
    con += 1
