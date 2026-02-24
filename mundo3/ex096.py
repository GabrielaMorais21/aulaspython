def area(largura, comprimento):
    s = largura * comprimento
    print('=' * 30)
    print('    Controle de Terrenos    ')
    print('=' * 30)
    print(f'A área de um terreno de {largura}x{comprimento} é de {s}m²')


# PROGRAMA PRINCIPAL    
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)