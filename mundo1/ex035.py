print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)
r1 = int(input('1° Seguimento: '))
r2 = int(input('2° Seguimento: '))
r3 = int(input('3° Seguimento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Pode FORMAR um triângulo.')
else:
    print('NÃO pode FORMAR um triângulo.')