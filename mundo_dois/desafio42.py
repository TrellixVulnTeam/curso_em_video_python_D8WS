a = int(input('Lado um:'))
b = int(input('Lado dois:'))
c = int(input('Lado três:'))
if (a < b + c) and (b < a + c) and (c < b + a):
    if a == b and b == c:
        print('É um triângulo Equilatero.')
    elif (a != b) and (a !=c) and (b != c):
        print('É um triângulo Escaleno.')
    elif (a == b and b != c) or (a == c and c != b) or (c == b and b !=a):
        print('É um triângulo Isóceles')
else:
    print('Não é um triângulo!')




