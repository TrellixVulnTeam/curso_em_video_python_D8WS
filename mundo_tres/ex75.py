tupla = (int(input('Digite um número:')), int(input('Digite um número:')),
        int(input('Digite um número:')), int(input('Digite um número:')),
        )

print('O número nove aparece:', tupla.count(9))

if 3 in tupla:
    print(f'O valor três apareceu na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado!')

print('Números pares:')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')




