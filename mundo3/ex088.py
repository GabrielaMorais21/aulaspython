from random import randint
from time import sleep
print('=' * 40)
print('JOGA NA MEGA SENA'.center(40))
print('=' * 40)
lista = []
jogadas = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {jogadas} Jogos...')
print('-' * 40)
for j in range(0, jogadas):
    for c in range(0, 6):
        nums = randint(1,60)
        lista.append(nums)
    print(f'Jogo {j + 1}: {lista}')
    sleep(1)
    lista.clear()
print('{:=^40}'.format(' < BOA SORTE! > '))
