preço = float(input('Qual o valor do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, com o desconto passou a valer R${:.2f}'.format(preço, novo))