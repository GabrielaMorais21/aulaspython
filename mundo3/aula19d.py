pessoas = {'Nome': 'Gabriela', 'Idade': 19, 'sexo': 'Feminino'}
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():    # COM DICIONÁRIOS USA-SE O ITEMS (como se fosse o enumerate)
    print(f'{k} = {v}')     
