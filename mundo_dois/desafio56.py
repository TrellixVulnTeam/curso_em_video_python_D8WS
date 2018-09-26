soma_idade = 0
media_idade = 0
maioridade_homem = 0
nome_maisvelho = ''
quantidade_mulher = 0
maioridade = 0

for p in range(1, 5):
    print('-----{}ª Pessoa-----'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))

    if p == 1 and sexo in 'Mm':
            maioridade_homem = idade
            nome_maisvelho = nome

    if idade > maioridade_homem and sexo in 'Mm':
            maioridade_homem = idade
            nome_maisvelho = nome

    if idade <= 20 and sexo in 'Ff':
        quantidade_mulher += 1

    soma_idade += idade

media_idade = soma_idade / 4

print('A media de idade: {}'.format(media_idade))
print('Nome do homem mais velho {} e idade {}'.format(nome_maisvelho, maioridade_homem))
print('Quantidade de mulheres maior ou igual a 20 anos: {}'.format(quantidade_mulher))




