n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(n, tot))
if tot == 2:
    print('É um número primo.'.format(n))
else:
    print('Não é um número primo.')
