import random
palpite = 0
numero = random.randint(1, 10)
print('Vou pensar um número, você consegue adivinhar ?')
tentativa = 0

while tentativa != numero:
    tentativa = int(input('Escolha um numero de 1 a 10:'))
    palpite += 1
    if tentativa > numero:
        print('É um número menor!')
    else:
        print('É um número maior!')

print('Você acertou! Eu pensei em  {} você escolheu {} e você deu {} palpites.'.format(numero, tentativa, palpite))
