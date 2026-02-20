pessoas = {'Nome': 'Gabriela', 'Idade': 19, 'sexo': 'Feminino'}
pessoas['Nome'] = 'Maria'     # MODIFICANDO O VALOR DA CHAVE
pessoas['peso'] = 68.2      # ADIOCIONANDO UMA NOVA CHAVE E VALOR 
for k, v in pessoas.items():
    print(f'{k} = {v}')
