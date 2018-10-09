mm = total = menor = c = 0
barato = ''
while True:
    nome = str(input('Nome do produto:'))
    p = float(input('Preço do produto:'))
    total += p
    c += 1
    r = 'b'
    if p > 1000:
        mm += 1
    if c == 1:
        menor = p
        barato = nome
    else:
        if p < menor:
            menor = p
            barato = nome
    while r not in 'sn':
        r = str(input('Deseja continuar?')).strip().lower()[0]
    if r == 'n':
        break


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(f'Total da compra: R$ {total:.2f}')
print(f'Total de produtos maior de R$ 1000: {mm}')
print(f'Produto mais barato é o/a {barato} e custa R$ {menor:.2f}')
