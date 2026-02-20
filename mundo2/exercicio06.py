senha_correta = 'python123'
senha_digitada = str(input('Digite sua senha: ')).strip().lower()
while senha_digitada != senha_correta:
    print('Senha incorreta.')
    senha_digitada = str(input('Digite novamente: ')).strip().lower()
print('Acesso Liberado.')