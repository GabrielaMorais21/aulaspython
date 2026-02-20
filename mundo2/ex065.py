resp = 'S'
media = cont = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média é {}.'.format(cont,media))
print('O menor número é {} e o maior é {}.'.format(menor, maior))
