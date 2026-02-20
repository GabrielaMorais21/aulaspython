from random import randint 
from time import sleep 
computador = randint(1,10)
quantidade = 1 
print('Tente adivinhar o mesmo número que eu de 1 a 10.')
print('Processando...')
sleep(2)
print('Pronto! Já fiz minha escolha. Agora é a sua vez!')
jogador = int(input('Faça sua escolha de 1 á 10: '))
while not jogador == computador:
    if computador > jogador: 
        print('Mais... Tente mais uma vez. ')
        jogador = int(input('Qual seu palpite? '))
    if computador < jogador:
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual seu palpite? '))
    quantidade += 1
print('Você escolheu o número {} e eu escolhi {}. PARABÉNS!!.'.format(jogador, computador))
print('Você tentou uma quantidade de {} vezes para acertar o mesmo que o meu.'.format(quantidade))
