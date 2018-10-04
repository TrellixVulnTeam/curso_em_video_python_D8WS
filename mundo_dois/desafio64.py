c = s = n = 0
n = int(input('Digite um número( para parar digite 999):'))
while n != 999:
    c += 1
    s = n + n
    n = int(input('Digite um número( para parar digite 999):'))
print(' Soma: {}\n Números digitados: {}'.format(s, c))