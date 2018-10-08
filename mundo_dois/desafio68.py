import random
v = resultado = jogador = pc = 0
escolha = ''
print('>>>>>>> Jogo par ou ímpar <<<<<<<<<<<<<<')
while True:
    escolha = str(input('Par ou ímpar?')).lower().strip()
    jogador = int(input('Escolha um número de um até 5:'))
    pc = random.randint(1, 5)
    resultado = (jogador + pc)%2
    if escolha == 'par' or escolha == 'p':
        if resultado == 0:
            print(f' Computador:{pc}\n Você:{jogador}')
            print(f' Soma:{jogador + pc}\n Você ganhou!!')
            v += 1
        elif resultado != 0:
            print(f' Computador:{pc}\n Você:{jogador}')
            print(f' Soma:{jogador + pc}\n Você perdeu, até logo!!')
            break
    elif escolha == 'impar' or escolha == 'ímpar' or escolha == 'i':
        if resultado == 0:
            print(f' Computador:{pc}\n Você:{jogador}')
            print(f' Soma:{jogador + pc}\n Você perdeu, até logo!!')
            break
        elif resultado != 0:
            print(f' Computador:{pc}\n Você:{jogador}')
            print(f' Soma:{jogador + pc}\n Você ganhou!!')
            v += 1
    else:
        print('Escolha incorreta!')
print(f'Número de vitórias: {v}')



