print('{:=^40}'.format(' LOJAS M.G '))
valor = float(input('PREÇO DOS PRODUTOS: R$'))
print('''[ 1 ] DINHEIRO/CHEQUE
[ 2 ] DÉBITO 
[ 3 ] CRÉDITO até 2X
[ 4 ] CRÉDITO 3X ou MAIS''')
pag = int(input('FORMA DE PAGAMENTO: '))
if pag == 1:
    total = valor - (valor * 10 / 100)
elif pag == 2:
    total = valor - (valor * 5 / 100)
elif pag == 3:
    total = valor
    parcela = total / 2
    print('Sua compra de será parcelada em 2X SEM JUROS de R${:.2f}.'.format(parcela))
elif pag == 4:
    total = valor + (valor * 20 / 100)
    totpar = int(input('Quantas parcelas? '))
    parcela = total / totpar
    print('Sua compra de será parcelada em {}X de R${:.2f}.'.format(totpar, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))