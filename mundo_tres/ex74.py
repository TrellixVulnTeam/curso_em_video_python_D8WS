from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Valores sorteados:')
for cont in tupla:
    print(cont, end=' ')

print(f'\nMaior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')



