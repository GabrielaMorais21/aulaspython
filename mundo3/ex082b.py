num = list()
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar [S/N]? ')).strip()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(num): 
    if v % 2 == 0:    
        par.append(v)    
    else: #elif v % 2 == 1:   
        impar.append(v)    
print()
print(f'Números: {num}')
print(f'N° Par: {par}')
print(f'N° Ímpar: {impar}')
