matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = tsoma = maior = 0 
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('==' * 30 )
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:   # SOMA DOS VALORES PARES PARA TODA A MATRIZ
            spar += matriz[l][c]
    print()
print('==' * 30)
print(f'A soma dos números PARES é de: {spar}')

for l in range(0,3):    # SOMA DIRECIONADA A TERCEIRA COLUNA 
    tsoma += matriz[l][2] #***
print(f'A soma dos valores da terceira coluna é de: {tsoma} ')

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]    # MAIOR NÚMERO DA SEGUNDA LINHA 
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é de {maior}')
