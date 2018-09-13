import random


n1 = int(input("Escreva um número de 0 a 5:"))
n = random.randint(0,5)

if n1 == n:
    print("Você acertou!")

else:
    print("Você errou!!O número era {}".format(n))


