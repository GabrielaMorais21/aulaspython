salario = float(input('Qual o seu salário atual? Informe para saber seu aumento: R$'))
if salario >= 1250:
    dez = (salario * 10 / 100) + salario
    print('Com o aumento de dez porcento seu salário ficou R${:.2f}'.format(dez))
else: 
    quinze = (salario * 15 / 100) + salario
    print('Com o aumento de quinze porcento, seu salário ficou R${:.2f}'.format(quinze))