from math import radians, cos, sin, tan 
angulo = float(input('Digite um número de sua escolha: '))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO equivalente a: {:.2f}'.format(angulo, cosseno))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO equilavente a: {:.2f}'.format(angulo, seno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE equivalente a: {:.2f}'.format(angulo, tangente))