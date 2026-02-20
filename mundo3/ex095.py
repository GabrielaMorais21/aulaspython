jogadores = {}
lista_todos = []

while True:
    jogadores['nome'] = str(input('Nome da Jogadora: ')).strip()
    partidas = int(input(f'Quantas partidas {jogadores['nome']} jogou? '))
    todos_gols = [] # ADICIONAR A VARIÁVEL GOL DENTRO DO LOOP PARA QUE ELE REINICIE
    for p in range(0, partidas):
        todos_gols.append((int(input(f'Quantos gols na {p+1}° partida? '))))
        
    jogadores['gols'] = todos_gols
    jogadores['total'] = sum(todos_gols)    # COPIAR O DICIONÁRIO JOGADORES PARA QUE 
    lista_todos.append(jogadores.copy())    # NÃO ENTRE EM REPETICAÇÃO INFINITA
    print('--' * 25)                                  
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break 
print('==' * 25)


print(f'{"cod":<4} {"Nome":<10} {"gols":<15} {"total":<5}')
print('--' * 25)
for i, j in enumerate(lista_todos):
    print(f'{i:<4} {j["nome"]:<10} {str(j["gols"]):<15} {j["total"]:<5}')
print('--' * 25)

while True:
    busca = int(input('Mostrar dados de qual jogador? '))   # SELICIONA O ÍNDICE
    if busca == 999:
        break
    if busca >= len(lista_todos):
        print(f'ERRO!! Não existe jogadores com código {busca}!')   
    else: 
        print(f'-- LEVANTAMENTO DA JOGADORA {lista_todos[busca]["nome"]}')
        for i, g in enumerate(lista_todos[busca]['gols']):
            print(f'    No {i+1}° jogo fez {g} gols')
    print('-' * 40 )

print(' << VOLTE SEMPRE >> ')