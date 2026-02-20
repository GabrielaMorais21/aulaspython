frase = str(input('Digite uma frase para analise: ')).strip().upper()
print('A letras "A" está presente {} vezes.'.format(frase.count('A')))
print('A letra "A" está presente a primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "A" está presente a última vez na posição {}.'.format(frase.rfind('A')+1))