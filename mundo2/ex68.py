from random import randint 
v = 0
print('==' * 13 )
print('VAMOS JOGAR ÍMPAR OU PAR')
print('==' * 13)
tipo = 'PI'
while True:
    jogador = int(input('Escolha um número: '))
    npc = randint(0,11)
    total = jogador + npc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('ÍMPAR ou PAR [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {npc} e deu um total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            v += 1 
            print('Você venceu! Jogue novamente...')
        else:
            print('GAME OVER...')
            break
    if tipo == 'I':    
        if total % 2 == 1:
            v += 1
            print('Você venceu! Jogue novamente...')    
        else:
            print('GAME OVER...')
            break 
print(f'Você venceu {v} vezes.')
    