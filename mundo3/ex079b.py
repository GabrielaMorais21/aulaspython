numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resp = str(input('Quer continuar? [S/N] '))
    if resp == 'Nn':
        break
print('=' * 30)
print(f'Você adicionou os valores {numeros}')