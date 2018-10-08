n = c = tabuada = 0

while True:
    n = int(input('Digite um númeor[número negativo para parar]:'))

    if n >= 0:
        for c in range(0, 11):
            tabuada = n * c
            print(f'{n} x {c} = {tabuada}')
    else:
        print('Volte sempre!')
        break
