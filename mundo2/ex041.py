from datetime import date 
data = int(input('''Informe seu ano de nascimento para descobrir em 
qual categoria irá participar da competição de natação: '''))
atual = date.today().year
idade = atual - data
if idade <= 9 :
    print('Categoria: MIRIM.') 
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
elif idade > 25:
    print('Categoria: MASTER.')