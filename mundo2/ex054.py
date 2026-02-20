from datetime import date 
atual = date.today().year
maiores = 0
menores = 0
for c in range(1,8):
    nasc = int(input('Ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maiores += 1 
    else:
        menores += 1
print('{} pessoas já são MAIORES de idade.'.format(maiores))
print('{} pessoas são MENORES de idade.'.format(menores))