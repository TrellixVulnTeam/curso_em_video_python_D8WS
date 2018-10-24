palavras =('aprender','estudar','dançar', 'jogar', 'dormir', 'escrever', 'ler', 'quadrado', 'alegria')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')