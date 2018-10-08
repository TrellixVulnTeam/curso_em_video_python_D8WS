idade = maior = m = f = 0
sexo = nome = r =''

while True:
    nome = str(input('Nome:')).lower().strip()
    idade = int(input('Idade:'))

    while sexo not in 'mf':
        sexo = str(input('Sexo[M/F]:')).lower().strip()
    if idade > 18:
        maior += 1
    if sexo in 'm':
        m += 1
    if sexo in 'f' and idade < 20:
        f += 1

    while r not in 'sn':
        r = str(input('Deseja comtinuar?')).lower().strip()
    if r == 'n':
        break

print(f' Maiores de 18: {maior}\n Quantidade do sexo masculino: {m}\n sexo feminino e menos de 20: {f}')



