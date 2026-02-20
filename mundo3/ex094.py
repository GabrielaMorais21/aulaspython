lista_dados = []
dados = {}
while True: 
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if dados['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas F ou M. ')
    dados['idade'] = int(input('Idade: '))
    lista_dados.append(dados.copy())
    while True: 
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('INVÁLIDO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 25)
print(f'- O grupo tem {len(lista_dados)} pessoas.')


soma_idades = sum(dados['idade'] for dados in lista_dados)
media = soma_idades / len(lista_dados)
print(f'- A média de idade é de {media:.2f} anos.')

print('- As mulheres cadastradas foram: ', end='')
for dados in lista_dados:
    if dados['sexo'] == 'F':
        print(f'{dados['nome']} ', end='')

print('\n- Lista das pessoas que estão acima da média: ')
print()
for dados in lista_dados:
    if dados['idade'] > media:
        for k, i in dados.items():
            print(f'{k} = {i}; ',end='')
print('\n  << ENCERRADO >>  ')