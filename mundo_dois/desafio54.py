maior_idade = 0
menor_idade = 0
for p in range(1, 7):
    idade = int(input('Idade da pessoa número {}:'.format(p)))
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('Quantidade de pessoas que atingiram a maior idade: {}'.format(maior_idade))
print('Qunatidade de pessoas que não atingiram: {}'.format(menor_idade))