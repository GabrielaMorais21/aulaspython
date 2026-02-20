valores = list()
for v in range(0,5):
    valores.append(int(input(f'valor para a posição {v}: ')))
print('=' * 30)
print(f'Você digitou os valores {valores}')

max = max(valores)
print(f'O maior valor é {max} e se encontra na posição ', end='')
for pos, c in enumerate(valores):
    if c == max:
        print(f'{pos}...', end=' ')

min = min(valores)
print(f'\nO menor valor é {min} e se escontra na posição ', end='')
for pos, c in enumerate(valores):
    if c == min: 
        print(f'{pos}...', end=' ')
