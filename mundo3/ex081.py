valor = list()
while True: 
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'S':
        continue
    elif resp == 'N': 
        break
print('-=' * 22 )
qtd = len(valor)
print(f'Você digitou {qtd} elementos.')
valor.sort(reverse=True)
print(f'Ordem decrescente: {valor}')
cinco = valor.count(5)
if cinco == True: 
    print('O número 5 foi digitado e aparece na lista.')
else:
    print('O número 5 não foi digitado.')
