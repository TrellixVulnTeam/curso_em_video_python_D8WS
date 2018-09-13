n1 = int(input("Escreva o número 1:"))
n2 = int(input("Escreva o número 2:"))
n3 = int(input("Escreva o número 3:"))

if n3 == n1 == n2:
    print("Os número são iguais!")
elif n1 >= n2 >= n3:
    print(" Maior: {}\n Menor:{}".format(n1, n3))
elif n1 >= n3 >= n2:
    print(" Maior: {}\n Menor: {} ".format(n1, n2))
elif n2 >= n1 >= n3:
    print(" Maior: {}\n Menor: {}".format(n2, n3))
elif n2 >= n3 >= n1:
    print(" Maior: {}\n Menor: {}".format(n2, n1))
elif n3 >= n2 >= n1:
    print(" Maior: {}\n Menor: {}".format(n3, n1))
elif n3 >= n1 >= n2:
    print(" Maior: {}\n Menor: {}".format(n3, n2))




