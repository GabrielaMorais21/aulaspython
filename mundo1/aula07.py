#n = input('Qual seu nome? ')
#print('Prazer em te conhecer {:->20}!'.format(n))
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2 
m = n1 - n2
p = n1 * n2 
d = n1 / n2 
po = n1 ** n2
di = n1 // n2
r = n1 % n2
print('O resultado da soma é: {}\n O resultado da subtração é: {}\n O resultado do produto é: {}\n O resultado da divisão é: {:.3f}\n O resultado da potência é: {} \n O resultado da divisão inteira é: {}\n O resultado restante da divisão é:{}'.format(s, m, p, d, po, di, r))
