pessoas = list()
dados = list()
mai = men = 0
while True: 
    dados.append(str(input('NOME: ')))
    dados.append(float(input('PESO: ')))
    peso_atual = dados[1]
    if len(pessoas) == 0: 
        mai = men = peso_atual
    else:
        if peso_atual > mai:
            mai = peso_atual
        if peso_atual < men:
            men = peso_atual
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if resp == 'S':
        continue 
    else:
        break
print('==' * 30)
print(f'Ao todo, {len(pessoas)} pessoas se cadastraram.')
print(f'O MAIOR peso foi de {mai}KG. Peso de ',end='')
for p in pessoas: 
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print(f'\nO MENOR peso foi de {men}KG. Peso de ',end='')
for f in pessoas:
   if f[1] == men:
       print(f'[{f[0]}] ',end='') 
 