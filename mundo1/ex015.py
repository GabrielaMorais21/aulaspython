dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
td = (dias * 60) + (km * 0.15)
print('O total a ser pago pelo carro alugado é de R${:.2f}'.format(td))
