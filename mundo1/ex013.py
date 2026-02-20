salario = float(input('Qual seu atual salário? R$'))
ns = salario + (salario * 15 / 100)
print('Seu novo salário com o acréscimo de 15% é de R${:.2f}'.format(ns))