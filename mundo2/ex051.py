print('==' * 12)
print('10 TERMOS DE UMA P.A')
print('==' * 12)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10) * razao
for c in range(termo, decimo, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')