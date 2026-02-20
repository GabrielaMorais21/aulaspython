from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
npc = randint(0,2)
print('''Escolha
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[npc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if npc == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Opção Inválida.')
elif npc == 1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Opção Iválida.')
elif npc == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opção Inválida.')