n = 0
while True:
    print('--' * 17)
    n = int(input('Quer ver a Tabuada de qual valor? '))
    print('--' * 17)
    if n < 0:
        break
    for c in range(1,11): 
        print(f'{n} X {c} = {n*c}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
