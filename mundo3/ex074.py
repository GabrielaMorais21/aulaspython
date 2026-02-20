from random import randint
num = randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20)
print(f'Números Gerados: ')
for n in num: 
    print( n, end=' | ')
print(f'\nMAIOR: {max(num)}')
print(f'MENOR: {min(num)}')
