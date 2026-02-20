num = [[], [] , []]
n = 0
for c in range(1,8):
    n = int(input(f'{c}° número: '))
    num[0].append(n)
    if n % 2 == 0:
        num[1].append(n)
    else:
        num[2].append(n)

print('==' * 25)
print(f'Todos os números são: {sorted(num[0])}')
print(f'PARES: {sorted(num[1])}')
print(f'ÍMPARES: {sorted(num[2])}')
