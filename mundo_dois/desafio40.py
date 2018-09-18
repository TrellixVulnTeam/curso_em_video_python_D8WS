n1 = float(input('Nota um:'))
n2 = float(input('Nota dois:'))
m = (n1+n2) / 2

if m < 5:
    print('Reprovado!')
elif (m >=5) and (m <= 6.9):
    print('Recuperação.')
elif m >= 7:
    print('Aprovado!')
