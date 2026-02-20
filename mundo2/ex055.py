maiorp = 0 
menorp = 0
for p in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print('O manor peso foi de {}Kg.'.format(menorp))
print('O maior peso foi de {}Kg.'.format(maiorp))