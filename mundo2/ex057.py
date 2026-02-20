sexo = str(input('Informe seu sexo: [F/M]')).strip().upper()[0]
while sexo not in 'MF': #enquanto sexo NÃO SER/ESTIVER EM.... "f/m"
    sexo = str(input('Dados inválidos. Digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
