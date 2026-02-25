from time import sleep
def contador(i,f,p):
    if p < 0:
        abs(p)
    if p == 0:
        p = 1
    print('-=' * 25)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1.5)

    if i <= f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# PROGRAMA PRINCIPAL

contador(1,10,1)
contador(0,10,2)
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passos: '))
contador(inicio, fim, passo)