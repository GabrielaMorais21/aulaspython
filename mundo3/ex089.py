aluno_nota = []
media = 0
while True: 
    print('==' * 20)
    nome = str(input('NOME: '))
    n1 = float(input('1° NOTA: '))
    n2 = float(input('2° NOTA: '))
    media = (n1 + n2) / 2
    aluno_nota.append([nome, [n1 ,n2], media])  # LISTA COMPOSTA 
    resp = str(input(f'Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        print('=-' * 20)
        print('No.  NOME       MÉDIA')
        break
    else: 
        continue 
for pos, n in enumerate(aluno_nota):
    print(f'{pos:<4} {n[0]:<10} {n[2]:<15.1f}')  
print('--' * 20)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(aluno_nota) - 1:
        print(f'As notas de {aluno_nota[opc][0]}são {aluno_nota[opc][1]}')
        print('--' * 20)
