
vc = float(input('Qual é o valor da casa?'))
s = float(input('Qual é o salário do comprador?'))
anos = int(input('Em quantos anos ele vai pagar a casa?'))
meses = anos * 12
p = vc / meses
e = (s * 30)/100
if p <= e:
    print(' prestações:{} de R$ {:.2f}'.format(meses, p))
    print(' 30 porcento do salário: R$ {:.2f}'.format(e))
    print(' O emprestimo foi aprovado!')
else:
    print(' meses: {}\n prestações:{} de R$ {:.2f}'.format(meses, meses, p))
    print(' 30 porcento do salário: R$ {:.2f}'.format(e))
    print(' O emprestimo foi negado!')

