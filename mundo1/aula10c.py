n1 = float(input('1° NOTA: '))
n2 = float(input('2° NOTA: '))
s = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(s))
if s >= 6: 
    print('Parabéns! Sua nota foi boa!')
else: 
    print('Sua nota foi ruim. Estude mais da próxima :(')