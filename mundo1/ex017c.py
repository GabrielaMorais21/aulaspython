import math 
ca = float(input('Qual a medida do cateto adjacente? '))
co = float(input('Qual a medida do cateto oposto? '))
hi = math.hypot(co, ca)
print('A hipotenusa é equivalente a {:.2f}'.format(hi))
