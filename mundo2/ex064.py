n = soma = 0
contagem = 1
print('Digite os números desejados. (CONDIÇÃO DE PARADA = 999)')
n = int(input('{}° número: '.format(contagem)))
while n != 999:
    soma += n
    contagem += 1
    n = int(input('{}° número: '.format(contagem)))
print('A quantidade de números foi de {} e a soma deles é {}'.format(contagem, soma))