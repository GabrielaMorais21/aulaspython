from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.now().year
dados['Idade'] = ano_atual - nascimento
CT = int(input('Carteira de Trabalho (Não tem = 0): '))
if CT != 0:
    dados['CTPS'] = CT
    dados['Contratação'] = int(input('Ano de Contração: '))
    dados['Salário'] = float(input('Salário: R$'))
# CALCULAR ANO DE APOSENTADORIA minima de 30 anos para MULHERES 
# 1° ano atual - ano de contratação
    # Tempo de trabalho
    tempo_trabalhado = ano_atual - dados['Contratação'] 
# 2° tempo mínimo de contribuição - tempo de trabalho 
    # tempo restante de trabalho para a aposentadoria 
    faltam = 30 - tempo_trabalhado
# 3° Idade atual + tempo restante para aposentar 
    # IDADE PARA APOSENTAR 
    dados['Aposentadoria'] = faltam + dados['Idade']
print('==' * 30)
print(dados)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')
