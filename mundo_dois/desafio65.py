r = 'sim'
soma = n = c = maior = menor = 0

while r in 'sim':
    n = float(input('Digite um número:'))
    r = str(input('Deseja continuar?')).lower().strip()[0]
    soma += n
    c += 1
    if c == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

m = soma / c
print('Média: {}'.format(m))
print(' Maior: {}\n Menor:{}'.format(maior, menor))