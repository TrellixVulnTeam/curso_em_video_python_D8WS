soma = 0
cont = 0
for c in range(1, 7):
     n = int(input('Escreva o {} número:'.format(c)))
     if n % 2 == 0:
         soma += n
         cont += 1
print(' Números pares: {}\n soma dos números pares: {}'.format(cont, soma))



