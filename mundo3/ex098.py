# SEI LÁ QUE CARALHO EU ARRUMEI AQUI... 
# JÁ ME ESTRESSEI DE SONO PQ MINHA CABEÇA NÃO TÁ FUNCIONANDOOOOO AAAAAA

from time import sleep
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for cont1 in range(1,11):
    print(f'{cont1}', end=' ', flush=True)
    sleep(0.1)
print('FIM!')
print('-=' * 20)
sleep(0.1)
print('Contagem de 10 até 0 de 2 em 2')
for cont2 in range(10,-1,-2):
    print(f'{cont2}', end=' ', flush=True)
    sleep(0.1)
print('FIM!')
print('-=' * 20)
sleep(0.1)
print('Agora é sua vez de personalizar a contagem!')
def contador(inicio, fim, passo):
    for escolhas in range (inicio, fim, passo):
        if passo == 0:
            passo = 1
        if passo < 0:
            abs(passo)
            print('-=' * 20)    
            sleep(1.5)
            if fim > inicio:
                fim -= passo
            print(f'{inicio} = {fim} = {passo}')
        print(f'Contagem de {inicio} de {fim}', end=' ', flush=True)
        sleep(0.2)
        if inicio < fim:
            cont = inicio
            while cont <= fim:
                print(f'{cont}', end=' ', flush=True)
                sleep(0.5)
                cont += passo
        #if fim < inicio:
        #    fim = inicio - passo
        print(inicio, escolhas + passo, end=' ', flush=True)
        print('FIM!')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, passo, fim)        # que coisa feia