n = int(input('Número:'))
print('Bases:\n [1]Binário\n [2]Octal\n [3]Hexadecimal')
base = int(input('Qual é a operação?'))

if base == 1:
    print('Binário:{}'.format(bin(n)))
elif base == 2:
    print('Octal:{}'.format(oct(n)))
elif base == 3:
    print('Hexadecimal:{}'.format(hex(n)))

