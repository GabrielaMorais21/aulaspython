lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else: 
        impar.append(n)
    resp = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if resp == 'S':
        continue 
    elif resp == 'N':
        break 
    else: 
        print('Resposta Inválida. Tente novamente.')
par.sort()
impar.sort()
print()
print(f'A lista completa é {lista}')
print(f'os números PAR: {par}')
print(f'os números ÍMPAR: {impar}')
