nums = int(input('1° VALOR: ')), int(input('2° VALOR: ')), int(input('3° VALOR: ')), int(input('4° VALOR: '))
print(f'Você digitou os valores: {nums}')
print(f'O número 9 apareceu {nums.count(9)}x.')
if 3 in nums:
    print(f'O número 3 aparece na posição {nums.index(3)+1}°.')
else:
    print('O valor 3 não foi digitado.')
print('Número PAR:', end=' ')
for p in nums:
    if p % 2 == 0:
        print(p, end=' ')
