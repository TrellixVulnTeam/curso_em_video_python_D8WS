listagem =('Borraacha', 1.75,
           'Lápis', 1,
           'Caderno', 33.90,
           'Estojo', 10.00,
           'Transferidor', 5.50,
           'Compasso', 4.90,
           'Mochila', 120.90,
           'Canetas', 2,
           'Livro', 34.90)

print('-'*40)
print('      LISTA DE PREÇOS')
print('-'*40)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
