lista = []

while True:
    n = int(input("Digite um valor:"))

    if n not in lista:
        lista.append(n)
    else:
        print("Valor duplicado!!")

    r = str(input("Deseja continuar?"))

    if r in 'nN':
        break

print("=-"*30)

lista.sort()
print(lista)



