times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 
         'Botafogo', 'Fluminense', 'Vasco', 'São Paulo', 'Corinthians', 
         'Grêmio', 'Bragantino', 'Atlético-MG', 'Ceará', 'Internacional', 
         'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport')
cont = 0
print('=' * 30)
print('{:^30}'.format('TABELA BRASILEIRÃO'))
print('=' * 30)
for t in times:
    cont += 1
    print(f'{cont}° {t}')
print('-=' * 25)
print(f'TOP 5 TABELA: {times[0:5]}')
print('-=' * 25)
print(f'ÁREA DE REBAIXAMENTO: {times[15:20]}')
print('-=' * 25)
print(f'ORDEM ALFABÉTICA: {sorted(times)}')
print('-=' * 25)
print(f'O Corinthians aparece no {times.index('Corinthians')+1}° lugar')