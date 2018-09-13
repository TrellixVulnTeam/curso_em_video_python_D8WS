d = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
v = (60*d)+(0.15*km)
print('O valor a ser pago é de R${:.2f}'.format(v))