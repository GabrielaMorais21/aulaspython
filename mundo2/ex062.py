print('-=' * 9)
print('Termos de uma P.A')
print('-=' * 9)
termo = int(input('TERMO: '))
razao = int(input('RAZÃO: '))
termo1 = termo
cont = 1 
total = 0
mais = 10
while mais != 0: 
    total += mais
    while cont <= total:
        print('{} → '.format(termo1), end='')
        termo1 += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais quer mostrar? '))
print('Foi mostrado um TOTAL de {} termos.'.format(total))
