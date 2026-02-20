nome = str(input('Digite seu nome completo: ')).strip() #strip para retirar os espaços desnecessários.
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('O seu nome completo tem um total de {} letras.'.format(len(nome) - nome.count(' ')))
#.format(len(nome.replace(' ', '')))) - outra forma que pode ser usada 
#print('Seu primeiro nome tem ao todo {} letras'.format(nome.find(' '))) - outra forma de ser usada
contador = nome.split()
print('O seu primeiro nome é {} e tem um total de {} letras.'.format(contador[0], len(contador[0])))