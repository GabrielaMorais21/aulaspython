numero1 = int(input('1° número: '))
numero2 = int(input('2° número: '))
numero3 = int(input('3° número: '))
menor = numero1 
if numero2 < numero3 and numero2 < numero1:
    menor = numero2
if numero3 < numero2 and numero3 < numero1:
    menor = numero3 
maior = numero1 
if numero2 > numero3 and numero2 > numero1:
    maior = numero2
if numero3 > numero2 and numero3 > numero1:
    maior = numero3 
print('O MAIOR número é {}'.format(maior))
print('O MENOR número é {}'.format(menor))
