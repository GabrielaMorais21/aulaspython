dados = {}
todos_gols = []
dados['nome'] = str(input('Nome do Jogador: ')).strip()
qtd_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for p in range(0, qtd_partidas):    
    todos_gols.append(int(input(f'Quantos gols na partida {p+1}: ')))
dados['gols'] = todos_gols[:]
dados['total'] = sum(todos_gols)  # SOMA DOS ITEMS DENTRO DE UMA LISTA
print('-=' * 20)
print(dados)
print('-=' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 20)
print(f'Jogador {dados["nome"]} jogou {qtd_partidas} partidas')

for i, v in enumerate(dados['gols']):       # PEGA OS DADOS DENTRO DO DICIONÁRIO QUE ESTÁ ESPECIFICANDO
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')
