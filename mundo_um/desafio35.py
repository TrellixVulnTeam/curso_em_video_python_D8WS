r1 = int(input("Reta um:"))
r2 = int(input("Reta dois:"))
r3 = int(input("Reta três:"))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("Forma um triângulo!")
else:
    print("Não forma um triângulo!")