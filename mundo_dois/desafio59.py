numero1 = float(input('Digete o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))
op = 0

while op != 5:
        print(' [1]Somar\n [2]Multiplicar\n [3]maior\n [4]novo número\n [5]Sair programa')
        op = int(input('>>>>>>> Qual a sua opção?'))

        if op == 1:
            print('Soma: {}'.format(numero1 + numero2))
        elif op == 2:
            print('Multiplicação: {}'.format(numero1 * numero2))
        elif op == 3:
            if numero1 > numero2:
                print('Número maior: {}'.format(numero1))
            else:
                print('Número maior: {}'.format(numero2))
        elif op == 4:
            numero1 = float(input('Digete o primeiro número:'))
            numero2 = float(input('Digite o segundo número:'))

        elif op == 5:
            print('Finalizando...')
        else:
            print('Opção inválida, digite novamente!')
        print('==' * 15)
print('O programa foi finalizado')


