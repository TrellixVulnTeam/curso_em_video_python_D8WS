tupla = ('zero','um','dois','três','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze','treze','catorze',
         'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


numero = int(input('Escreva um número entre 0 e 20:'))
while numero > 20 or numero < 0:
    print('Número entre 0 e 20!!')
    numero = int(input('Escreva um número entre 0 e 20:'))

print(tupla[numero])