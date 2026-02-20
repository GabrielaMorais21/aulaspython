v = float(input('Qual a velocidade indicada? '))
if v > 80.00:
    print('Você foi MULTADO!')
    multa = (v - 80) * 7
    print('Sua  multa é no valor de {}. Dirija com mais cuidado!'.format(multa))
else:
    print('Tudo de acordo. Tenha um ótimo dia!')