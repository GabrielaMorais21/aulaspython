maiorid = 0             # Fiz sozinha
generof = 0
while True:
    print('=' * 21)
    print('CADASTRE UMA PESSOA')
    print('=' * 21)
    idade = int(input('IDADE: '))
    genero = str(input('GÊNERO [F/M]: ')).strip().upper()[0]
    print('==' * 11)
    continua = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if genero == 'M':
        generom += 1 
    elif genero == 'F':
        if idade < 20:
            generof += 1 
    if idade > 18:
        maiorid += 1
    if continua == 'S':
        continue
    elif continua == 'N':
        break
    else:
        continua = str(input('Resposta INVÁLIDA. Digite novamente [S/N]: ')).strip().lower()[0]
print(f'{maiorid} pessoas tem mais de 18 anos.')
print(f'{generom} homens foram cadastrados')
print(f'{generof} mulheres foram cadastradas')
