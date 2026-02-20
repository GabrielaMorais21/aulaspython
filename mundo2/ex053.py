frase = str(input('Digite uma frase: ')).strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1 ):
    inverso += junto[letra]
if inverso == junto:
    print('A frase é um polímedro')
else:
    print('A frase NÃO é um polímedro')   