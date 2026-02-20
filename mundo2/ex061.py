print('-=' * 12)
print('10 TERMOS DE UMA P.A')
print('-=' * 12)
termo = int(input('TERMO: '))
razao = int(input('RAZÃO: '))
termo1 = termo 
cont = 1
print('Os 10 termos da progressão aritimética é: ')
while cont <= 10:
    print('{} → '.format(termo1), end='')
    termo1 += razao
    cont += 1
print('FIM')