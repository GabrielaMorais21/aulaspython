preço1 = float(input('1° VALOR: '))
preço2 = float(input('2° VALOR: '))
preço3 = float(input('3° VALOR: '))
menor = preço1
if preço2 < preço1 and preço2 < preço3:
    menor = preço2
if preço3 < preço1 and preço3 < preço2:
    menor = preço3
maior = preço1 
if preço2 > preço1 and preço2 > preço3:
    maior = preço2
if preço3 > preço1 and preço3 > preço2:
    maior = preço3 
print('O maior vlaor é R${:.2f}'.format(maior))
print('O menor valor é R${:.2f}'.format(menor))