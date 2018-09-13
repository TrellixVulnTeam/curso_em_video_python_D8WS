frase = str(input('Escreva uma frase:')).upper().strip()
print('O numero de "a" é {}'.format(frase.count('A')))
print('A primeira letra "a" aparece na posição {}"'.format(frase.find('A')+1))
print('A ultima letra "a" aparece na posição {}'.format(frase.rfind('A')+1-frase.count(' ')))
# +1 para n contar a partir do 0
#rfind para procurar da direita pra esquerda

