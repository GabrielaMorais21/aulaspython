senha_correta = 'python123'
tentativas = 0
limite = 3
while tentativas <= limite:
    senha_digitada = str(input('Senha: ')).strip().lower()
    if senha_digitada == senha_correta:
        print('Acesso Liberado. ')
        break
    else:
        print('Senha Incorreta.')
        tentativas += 1
if tentativas == limite:
    print('Número de tentativas atingido. Acesso Bloqueado.')