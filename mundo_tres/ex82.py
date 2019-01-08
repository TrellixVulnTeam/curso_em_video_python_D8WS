lista = []
par = []
impar = []

while True:
    n = int(input('Digite um número:'))
    lista.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    r = str(input('Deseja continuar? [S/N]'))
    if r in 'nN':
        break


print('-='*30)

print(f'Números digitados: {lista}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
