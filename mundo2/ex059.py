from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=' * 21)
    print('''[ 1 ] SOMA 
[ 2 ] MULTIPLICAÇÃO 
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA''')
    print('=' * 21)
    opcao = int(input('Opção desejada: ')) 
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos {} + {} é {}.'.format(n1, n2, soma))
    elif opcao == 2: 
        produto = n1 * n2
        print('O produto de {} X {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        else:
            print('O maior número é {}.'.format(n2))
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim do programa. Volte sempre ') 
