termo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = termo +(10 -1) * razao
print('A pa é:')
for c in range(termo, decimo, razao):

   print('{}'.format(c), end=', ')

