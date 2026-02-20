n = int(input('Digite um número qualquer: '))
ip = n % 2 
if ip == 1:
    print('{} é um número ÍMPAR.'.format(n))
else:
    print('{} é um número PAR.'.format(n))