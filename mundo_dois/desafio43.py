nome = str(input('Qual é seu nome?'))
p = float(input('Qual é o seu peso?'))
a = float(input('Qual é sua altura?'))
imc = p / (a * a)

if imc < 18.5:
    print('Você esta abaixo do peso {}.'.format(nome))
elif (imc >= 18.5) and (imc <= 25):
    print('Você está no peso ideal {}.'.format(nome))
elif (imc > 25) and (imc <=30):
    print('Você entá com sobrepeso {}'.format(nome))
elif (imc > 30) and (imc <= 40):
    print('Você está com obesidade {}'.format(nome))
elif imc > 40:
    print('Obesidade Mórbida.')
