from random import randint
print('''Opções:
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador = int(input('Qual será sua opção?'))
lista = ['Peadra', 'Papel', 'Tesoura']
computador = randint(0, 2)

if jogador == 0 or jogador == 1 or jogador == 2:
    print(''' JO
 KEN
 PO!''')
    print('o Computador escolheu {}'.format(lista[computador]))
    print('O jogador escolheu {}'.format(lista[jogador]))
    if computador == 0: #Computador escolheu pedra
        if jogador == 0:
            print('Empatou!')
        elif jogador == 1:
            print('Você ganhou!!')
        elif jogador == 2:
            print('Você perdeu :(')

    elif computador == 1: #Computador escolheu papel
        if jogador == 1:
            print('Empatou!')
        elif jogador == 0:
            print('Você perdeu :(')
        elif jogador == 2:
            print('Você Ganhou!!')
    elif computador == 2: #Computador escolheu tesoura
        if jogador == 2:
            print('Empatou!')
        elif jogador == 0:
            print('Você ganhou!!')
        elif jogador == 1:
            print('Você perdeu :(')
else:
    print('Jogada inválida!!')


