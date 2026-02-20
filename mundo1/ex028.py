import random 
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
num = random.randint(1, 5)
escolha = int(input('Em que número eu pensei? '))
if num == escolha:
    print('PARABÉNS!! Você ACERTOU o número!')
    print('O número escolhido pelo computador também foi {}'.format(num))
else:
    print('Não foi desa vez... tente novamente.')
    print('O número escolhido pelo programa foi: {}'.format(num))
