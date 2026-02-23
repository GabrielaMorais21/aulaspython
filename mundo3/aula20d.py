def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print(' FIM!')

contador(2, 1, 7)
contador(8, 0)          # cria uma túpla com os valores 
contador(4, 4, 7, 6, 2)
