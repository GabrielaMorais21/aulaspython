produtos = ('Carne', 67.98, 'Carvão', 12.00, 'Cerveja', 84.00,
            'Coca-Cola', 13.00, 'Sal Grosso', 08.00, 'Pão de Alho',
            28.00, 'Gelo', 10.00, 'linguiça', 21.50, 'Churrasqueira', 115.00)
print('=' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('=' * 50)
for p in range(0, len(produtos), 2):
    nome = produtos[p]
    preço = produtos[p+1]
    print(f'{nome:.<50} R${preço:.2f}')