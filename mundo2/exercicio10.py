from random import randint 
from time import sleep
npc = randint(1,10)
jogador = 0
print('-=' * 16)
print('Tente adivinha o mesmo número que Eu.')
print('-=' * 16)
print('Processando...')
sleep(3)
while jogador != npc:
    jogador = int(input('Digite sua escolha: '))
    if jogador != npc:
        print('Não foi dessa vez. Tente novamente.')
print('Você acertou!! A minha escolha também foi {}'.format(npc) )