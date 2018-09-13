import math
co = float(input('Qual é o valor do cateto oposto?'))
ca = float(input('Qual é o valor do cateto adjacente?'))

h = math.hypot(co, ca)

print('O valor da hipotenusa é {:.2f}'.format(h))



