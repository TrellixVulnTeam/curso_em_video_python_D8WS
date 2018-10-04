n = int(input('Quantos termos você quer mostrar?'))
c = 0
t1 = 0
t2 = 1
t3 = 0
print('sequência de Fibonacci:')
while c < n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print('{}'.format(t3), end='')
    print(', ' if c < n else '', end='')
