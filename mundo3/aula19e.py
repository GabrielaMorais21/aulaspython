pessoas = {'Nome': 'Gabriela', 'Idade': 19, 'sexo': 'Feminino'}
del pessoas['sexo']     #   APAGA A CHAVE TOTALMENTE 
for k, v in pessoas.items(): 
    print(f'{k} = {v}')  
