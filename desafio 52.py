num = int(input('\nDigite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='\033[m')
if tot == 1:
    print('\n\nO número {} foi divisível somente uma vez'.format(num), end=' ')
else:
    print('\n\nO número {} foi divisível {} vezes'.format(num, tot), end=' ')
if tot == 2:
    print('e, por isso, ele é primo.')
else:
    print('e, por isso, ele \033[31mnão\033[m é primo.')
