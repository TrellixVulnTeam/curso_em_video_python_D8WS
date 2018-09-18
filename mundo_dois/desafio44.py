vp = float(input('Valor do produto:'))
print('''Formas de pagamento:
[1]Dinheiro
[2]Cheque
[3]Cartão''')
fp = int(input('Forma de pagamento:'))

if (fp == 1) or (fp == 2):

    parcelas = int(input('Quantas vezes:'))

    if parcelas == 1:
        vt = vp - (vp * 10 / 100)
        print('Valor com desconto de 10%: R$ {:.2f}'.format(vt))
    else:
        print('No dinheiro ou cheque só pode uma parcela!')
elif fp == 3:
    parcelas = int(input('Quantas vezes:'))
    if parcelas == 1:
        vt = vp - (vp * 5 / 100)
        print('Valor com desconto de 5%: R$ {:.2f}'.format(vt))
    elif parcelas == 2:
        pt = vp / 2
        print('Valor de R$ {:.2f} sem desconto: 2 x de R$ {:.2f}'.format(vp, pt))
    elif parcelas >= 3:
        vt = vp + (vp * 20 / 100)
        pt = vt / parcelas
        print('Valor de R$ {:.2f} com juros de 20%: {} x R$ {:.2f} '.format(vt, parcelas, pt))
else:
    print('Forma de pagamento inválida!')



