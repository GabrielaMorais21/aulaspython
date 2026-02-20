frase = str(input('FRASE: ')).strip().lower()
print('A letra "A" aparece {} vezes'.format(frase.count('a')))
print('A primeira vez que aparece "A" é em {}'.format(frase.find('a')+1))
print('A última vez que aparece "A" é {}'.format(frase.rfind('a')+1))