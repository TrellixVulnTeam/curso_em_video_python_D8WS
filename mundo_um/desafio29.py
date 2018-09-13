v = int(input("Qual foi a velocidade do carro em Km?"))

if v > 80:
    vm = v - 80
    m = vm * 7
    print("Você foi multado!!Você vai receber R$ {:.2f}".format(m))
else:
    print("Você não foi multado.")

