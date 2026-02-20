from datetime import date 
atual = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
genero = str(input('Informe seu gênero (F/M): ')).strip().lower()
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if genero == 'f':
    print('O alistamento no exército não é obrigatório para mulheres.')
    voluntario = input('Você deseja se alistar no exército (S/N)? ').strip().lower()
    if voluntario == 'n':
        print('O processo de alistamento foi encerrado.')
    elif voluntario == 's':
        if idade > 18:
            falta = idade - 18
            ano = atual - falta 
            print('Você deveria ter se alistado em {} há {} anos atrás.'.format(ano, falta))
        elif idade < 18:
            falta = 18 - idade
            ano = atual + falta
            print('Você terá que se alistar daqui {} anos em {}.'.format(falta, ano))
        elif idade == 18:
            print('Você deve se alistar IMEDIATAMENTE.')
        else:
            print('Opção inválida. Use S ou N.')
elif genero == 'm':
    if idade > 18: 
        falta = idade - 18
        ano = atual - falta
        print('Você deveria ter se alistado há {} anos em {}.'.format(falta, ano))
    elif idade < 18:
        falta = 18 - idade
        ano = atual + falta
        print('Você terá que se alistar daqui {} anos em {}.'.format(falta, ano))
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE.')
    else:
        print('Opção inválida. Escolha S ou N.')
else: 
    print('Opção inválida. Escolha F ou M para continuar a análise.')
