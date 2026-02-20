n = int(input('Digite um número para ter a tabuada: '))
print('=' * 13)
print('Tabuada do {}'.format(n))
print('=' * 13)
for c in range(1, 11):
    soma = n * c
    print('{} X {} = {}'.format(c, n, soma))