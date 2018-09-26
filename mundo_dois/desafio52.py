n = int(input('EScreva um número:'))
nd = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end=' ')
        nd += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m0{} foi divisível {} vezes.'.format(n, nd))

if nd == 2:
    print('Ele é primo!!')
else:
    print('Ele não é primo!')
