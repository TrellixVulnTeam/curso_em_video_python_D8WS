s = float(input("Qual é o salário?"))

if s <= 1250:
    nv = s + (s * 15 / 100)
else:
    nv = s + (s * 10 / 100)

print("Novo salário é de R$ {:.2f}".format(nv))

