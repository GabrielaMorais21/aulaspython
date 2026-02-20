galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('NOME:  ')))
    dado.append(int(input('Idade:  ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
#print(dado)   DADOS DE 'dado' APAGADOS

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de 18 anos. ')
        totmai += 1
    else:
        print(f'{p[0]} é menor de 18 anos.' )
        totmen += 1 
print(f'Temos {totmai} pessoas maior de idade e {totmen} menor de 18 anos.')
