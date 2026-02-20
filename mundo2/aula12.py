nome = str(input('Qual é seu nome? ')).strip().lower()
if nome == 'gabriela':
    print('Que nome lindo!!')
elif nome == 'alanna' or nome == 'maria' or nome == 'carlos':
    print('nome de gostosa HAHAHA!!')
elif nome in 'ana claudia jessica julia bianca ':
 print('belo nome feminino')
else:
    print('Seu nome é normal..')
print('Tenha um bom dia {}!'.format(nome))
