d = int(input("Qual é a distância da viagem?"))

if d <= 200:
    v = d * 0.50
    print("O valor da viagem foi de R$ {:.2f}".format(v))
else:
    v = d * 0.45
    print("O valor da viagem foi de R$ {:.2f}".format(v))