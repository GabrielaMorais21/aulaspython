contagem = ('zero', 'um', 'dois', 'três', 'quatro', 
            'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
            'onze', 'doze', 'treze', 'catorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {contagem[num]}.')
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if resp == 'S':
            continue
        else:
            print('=' * 20)
            print('Programa encerrado.')
            print('=' * 20)
            break 
    else: 
        print('Tente novamente. ', end='')