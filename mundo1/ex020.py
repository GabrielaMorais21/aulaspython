from random import shuffle
n1 = str(input('Primeiro grupo: '))
n2 = str(input('Segundo grupo: '))
n3 = str(input('Terceiro grupo: '))
n4 = str(input('Quarto grupo: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)