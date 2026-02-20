casa = float(input('Qual o valor da casa? R$'))
renda = float(input('Qual a sua renda mensal? R$'))
anos = int(input('Em quantos ANOS deseja fazer a quitação da casa? '))
prestacao = casa / (anos * 12)
if prestacao > renda * 30 / 100:
    print('Seu empréstimo foi NEGADO. O valor da parcela excedeu 30 porcento da sua renda mensal.')
else: 
    print('PARABÉNS! Seu empréstimo foi aceito.')
print('a prestação da sua casa será {:.2f}'.format(prestacao))
