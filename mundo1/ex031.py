d = float(input('Qual a distância? '))
if d < 200:
    valor = d * 0.50
    print('O valor da passagem é de R${:.2f}.'.format(valor))
else: 
    valor = d * 0.45
    print('O valor da passagem é de R${:.2f}.'.format(valor))