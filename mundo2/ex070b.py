total = totmil = cont = menor = barato = 0
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:   # MANEIRA SIMPLIFICADA
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'Temos {totmil} produto que custa mais que R$1.000,00') 
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')
print(f'TOTAL: R${total:5.2f}')
