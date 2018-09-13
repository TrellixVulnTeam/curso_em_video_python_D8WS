a = int(input("Número um:"))
b = int(input("Número dois:"))
c = int(input("Número três:"))

# verificar quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# verificar quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(" maior: {}\n menor: {}".format(maior, menor))



