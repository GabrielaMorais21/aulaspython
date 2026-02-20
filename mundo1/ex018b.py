from math import radians, cos, sin, tan
angulo = float(input('Digite um número: '))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(angulo, cosseno))
seno = sin(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))
