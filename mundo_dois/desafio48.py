somatudo = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        somatudo = somatudo + n
        cont = cont + 1
print('foi solicitado {} números e a somadeles é {}'.format(cont, somatudo))
