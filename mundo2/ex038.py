num1 = int(input('1° número: '))
num2 = int(input('2° número: '))
if num1 > num2:
    print('O número {} é maior que {}.'.format(num1, num2)) 
elif num1 < num2:
    print('O número {} é maior que {}.'.format(num2, num1))
else:
    print('Os números {} e {} são IGUAIS'.format(num1, num2))