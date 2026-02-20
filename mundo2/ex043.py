#indíce de massa corporal 
altura = float(input('ALTURA: '))
peso = float(input('PESO: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Está ABAIXO do peso.')
elif imc <= 25:
    print('Está no peso IDEAL.')
elif imc <= 30:
    print('Está SOBREPESO.')
elif imc <= 40:
    print('Está com OBESIDADE.')
else:
    print('Está com OBESIDADE MÓRBIDA.')
print('Seu índice de massa corporal é de: {:.1f}'.format(imc))