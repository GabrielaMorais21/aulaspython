from time import sleep
print('=-' * 11)
print('Programa Iniciando...')
print('=-' * 11)
sleep(2)
valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else: 
        print('Valor duplicado! Não vou adicionar.')
    resp = str(input('Deseja continuar [S/N?] ')).strip().lower()[0]
    if resp == 's':
        continue 
    elif resp == 'n':
        break
    else: 
        print('Resposta Inválida. Tente novamente. ',end='')
valores.sort()
print('=' * 30)
print(f'Você digitou os valores: {valores}')    
