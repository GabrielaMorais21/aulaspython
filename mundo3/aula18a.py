teste = list()
teste.append('Gabriela')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Izabelle'
teste[1] = 17
galera.append(teste[:])
print(galera)