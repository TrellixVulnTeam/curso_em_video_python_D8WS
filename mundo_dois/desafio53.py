frase = str(input('Escreva uma frase:')).lower().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]


if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!!')

