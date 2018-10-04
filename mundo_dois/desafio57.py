sexo = str(input('Sexo:')).strip().upper()[0]
while sexo not in 'MmFf;':
    sexo = str(input('Digite um valor para o sexo válido:')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))