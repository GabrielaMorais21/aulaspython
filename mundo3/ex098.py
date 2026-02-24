from time import sleep
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for cont1 in range(1,11):
    print(f'{cont1}', end=' ', flush=True)
    sleep(0.5)
print('FIM!')
print('-=' * 20)
sleep(2)
print('Contagem de 10 até 0 de 2 em 2')
for cont2 in range(10,-1,-2):
    print(f'{cont2}', end=' ', flush=True)
    sleep(0.5)
print('FIM!')
print('-=' * 20)
sleep(2)
#def contador(inicio, fim, passo):

#inicio = int(input('Ínicio: '))
#fim = int(input('Fim: '))
#passo = int(input('Passo: '))