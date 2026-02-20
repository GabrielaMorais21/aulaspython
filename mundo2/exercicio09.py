con = 0
c = 1
soma = 0
while c != 0:
    con += 1
    c = int(input('''(Condição de parada = 0) 
    {}° número: '''.format(con)))
    soma += c
print('A soma dos números é {}'.format(soma))
