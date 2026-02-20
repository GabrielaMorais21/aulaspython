from random import randint 
from time import sleep
from operator import itemgetter
nums = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = []
print('Valores sorteados: ')
for k, v in nums.items():
    print(f'    O {k} tirou {v} no dado')
    sleep(1)
print('-=' * 25)
print('  == Ranking dos Jogadores == ')
ranking = sorted(nums.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
