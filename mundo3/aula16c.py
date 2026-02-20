lanche = 'hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita'

# 1°
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')
                           # MOSTRANDO A POSIÇÃO/INDENTAÇÃO DO OBJ/VAR
print('')
print('=' * 10)
print('')

# 2°
for comida in lanche:
    print(comida)
# na segunda maneira não é possível mostrar 
# a posição da mesma forma da primeira

print('')
print('=' * 10)
print('')

# 3° 
for comida in enumerate(lanche):
    print(f'{comida}') # COM PARÊNTESE 

print('')
print('=' * 10)
print('')

# 4°
for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}') # S/ PARÊNTESES DE FORMA LIMPA 


#  MANEIRAS DE EXECUTAR O MESMO PROGRAMA 