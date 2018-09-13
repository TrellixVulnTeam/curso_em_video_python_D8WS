import math
a = float(input('Qual é o ângulo?'))

seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))

print('Seno = {:.2f}'.format(seno))
print('cosseno = {:.2f}'.format(cosseno))
print('tangente = {:.2f}'.format(tangente))
