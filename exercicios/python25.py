from random import randint
from time import sleep

while True:
    computador = randint(0, 99)  # Faz o computador "pensar" em um número
    print('Vou pensar em um número entre 0 e 99. Tente adivinhar...')
    try:
        jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
    except ValueError:
        print('Entrada inválida. Digite um número inteiro entre 0 e 99.')
        continue

    print('PROCESSANDO...')
    sleep(3)  # Pausa de 3 segundos para criar suspense
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer!')
    else:
        print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

    resp = input('Quer jogar novamente? [S/N] ').strip().upper()
    if not resp or resp[0] != 'S':
        print('Fim do jogo! Volte sempre!')
        break