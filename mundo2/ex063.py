print('--' * 10)
print('Sequência Fibonacci')
print('--' * 10)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1 
print('{} → {} → '.format(t1,t2), end='')
cont = 3 
while cont <= n: 
    proximo = t1 + t2
    print('{} → '.format(proximo), end='')
    t1 = t2 
    t2 = proximo
    cont += 1 
print('FIM')
