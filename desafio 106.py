from time import sleep
cores = ('\033[m',          # fechar
         '\033[0;30;41m',   # vermelho
         '\033[0;30;42m',   # verde
         '\033[0;30;43m',   # amarelo
         '\033[0;30;44m',   # azul
         '\033[0;30;45m',   # roxo
         '\033[0;30;47m')   # branco


def ajuda(comando):
    título(f'Acessando o manual do comando \'{comando}\'', 4)  # \'{comando}'\ é usado para printar função sem executar
    print(cores[6])
    help(comando)
    print(cores[0])
    sleep(2)


def título(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(f'{cores[cor]}{"~"*tamanho}\n{mensagem}\n{"~"*tamanho}\n{cores[0]}', end='')
    sleep(1)


com = ''
while True:
    título('SAPH - Sistema de Ajuda PyHelp', 2)
    com = str(input('Digite uma função ou biblioteca > '))
    if com.upper() == 'FIM':
        break
    else:
        ajuda(com)
título('ATÉ MAIS!', 1)
