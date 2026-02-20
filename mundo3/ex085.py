num = [[] , []]
n = 0
for c in range(1,8):
    n = int(input(f'{c}° número: '))
    if n % 2 == 0:
        num[0].append(n)
    if n % 2 == 1:
        num[1].append(n)
print('==' * 30)
print(f'Os valores PARES digitados foram: {sorted(num[0])}')
print(f'Os valores ÍMPARES digitados foram: {sorted(num[1])}')
    