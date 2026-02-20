print('-=-' * 10)
print('ANALISADOR DE TRIÂNGULO 2.0')
print('-=-' * 10)
s1 = int(input('1° SEGUIMENTO: '))
s2 = int(input('2° SEGUIMENTO: '))
s3 = int(input('3° SEQUIMENTO: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('Os seguimentos podem formar um triângulos ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO.')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Não pode formar um triângulo.')
    