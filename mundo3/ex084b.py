pessoas = []
dados = []

while True:
    dados.append(str(input('NOME: ')))
    dados.append(float(input('PESO: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('==' * 30)
print(pessoas)