lista = []

while True:
    lista.append(int(input('Digite um valor:')))
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

print('-='*30)
print(f'Você digitou {len(lista)} elementos.')

lista.sort(reverse=True)

print(f'Lista valor decrescente: {lista}')

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista')
