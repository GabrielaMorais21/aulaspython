soma = 0
maisvelho = 0 
mulheres = 0
nomemaisvelho = ''
for p in range(1,5):
    print('=-=-=-= {}° PESSOA =-=-=-='.format(p))
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M): ')).strip().lower()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    else:
        if idade < 20: 
            mulheres += 1
media = soma / 4
print('A idade média desse grupo é de {}'.format(media))
print('O homem mais velho desse grupo tem {} anos e se chama {}.'.format(maisvelho, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))