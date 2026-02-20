b = float(input('Qual a largura da parede em metros? '))
h = float(input('Qual a altura da parede em metros? '))
a = b * h 
print('A área em metros quadrados da parede é de {}'.format(a))
t = a / 2
print('O total de litros de tinta necessários para pintar toda essa área é de {:.2f}L'.format(t))