nome = str(input('Qual é seu nome inteiro?')).strip()#Eliminar espaços antes e depois

print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))#Para não contar os espaços

