r = 'sim'

while r in 'sim':
    primeiro = int(input('Primeiro termo:'))
    razao = int(input('Razão:'))
    termo = primeiro
    c = 1
    print('Pa: ', end='')

    while c < 10:
        print('{}'.format(termo), end='')
        print(', 'if c < 9 else ' ', end='')
        termo += razao
        c += 1

    r = str(input('\nQuer continuar?')).lower().strip()[0]
    if r in 'nao':
        print('Até a proxima')