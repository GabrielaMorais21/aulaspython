import math
an = float(input('Digite um número que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o seno {:.2f}.'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o cosceno {:.2f}.'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a tangente {:.2f}.'.format(an, tangente))
