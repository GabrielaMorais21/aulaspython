tot = caro = maior = 0              # NÃO DEI CONTA de fazer o maior número... 
while True:
    produto = str(input('PRODUTO: '))
    valor = float(input('VALOR: R$'))
    tot += valor
    if valor > 1000:
        caro += 1 

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break 
print(f'{caro} produtos custam mais que R$1.000,00')
print(f'TOTAL: R${tot:.2f}')
