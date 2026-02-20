nota1 = float(input('PRIMEIRA NOTA: '))
nota2 = float(input('SEGUNDA NOTA: '))
media = (nota1 + nota2) / 2
print('Quem tirou a nota {:.1f} e {:.1f} tem uma média de {:.1f}.'.format(nota1, nota2, media))
if media >= 5 and media < 7:
    print('O aluno está de RECUPERAÇÃO.')
elif media >= 7:
    print('O aluno está APROVADO.')
else:
    print('O aluno está REPROVADO.')
