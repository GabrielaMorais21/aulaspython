import math 
ca = float(input('Qual a medida do cateto adjacente? '))
co = float(input('Qual a medida do cateto oposto? '))
hi = ca**2 + co**2 
print('O comprimento da hipotenusa é de {:.2f}'.format(math.sqrt(hi)))