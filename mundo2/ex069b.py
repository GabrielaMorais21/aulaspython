tot18 = 0               # AULA com Guanabara
sexm = 0
fem20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0] 
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        sexm += 1
    if sexo == 'F' and idade < 20:
        fem20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp == 'N':
        break 
print(f'total de pessoas com 18 anos ou mais: {tot18}')
print(f'Total de homens cadastrados: {sexm}')
print(f'Mulheres com menos de 20 anos: {fem20}')
